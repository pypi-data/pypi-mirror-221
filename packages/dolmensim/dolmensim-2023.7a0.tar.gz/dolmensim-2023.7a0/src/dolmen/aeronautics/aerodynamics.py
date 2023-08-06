# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:12:10 2022

@author: nicolas.rouve
"""

import math
import numpy as np

import dolmen.utils.PhysicsInt as pyi
import dolmen.mechanics.inertia as ia
import dolmen.mechanics.fluidsMechanics as fm

import dolmen.utils.dataTable as tbl

class Wing:
    """
    A class used to define a wing and get lift, drag, and moment

    Attributes
    ----------
    area: float
        wing area as read in AFM or other docs
    
    wingPerf: dolmen.utils.dataTable.dataFile
        parameter table giving the coefficient for various angle of attack
        Mandatory column are :
            - 'alpha' : angle of attack
            - 'CL' : Lift coefficient
            - 'CD' : Drag coeffient
            - 'CM' : pitch Moment coefficient
    """

    def __init__(self, area, coeffFileName):
        self.area = area
        self.wingPerf = tbl.dataFile(coeffFileName , 'alpha')
        # self.wingPerf = tbl.dataFile("C:/Users/nicolas.rouve/Documents/20_PROJETS/PYTHON/DOLMEN/Ask21Wing.csv", 'alpha')


    def getLift(self, velocity, alpha, rho = 1.225):
        """
        function for the calculation of the lift force of a wing according to angle of attack
        
        Parameters
        ----------
        velocity : float
            relative velocity of the air on the wing 
        alpha : float
            angle on attack i.e. angle between air direction an wing chord (theta + i_w)
        rho : float [optional]
            air density in kg/m^3
        """
        CL=self.wingPerf.getParam(alpha, 'CL')
        # print(f">> Wing::getLift : alpha={alpha}, CL={CL}")
        L = CL *((rho*velocity**2)/2)*self.area
        return L # portance_aile

    def getDrag(self, velocity, alpha, rho = 1.225):
        """
        function for the calculation of the drag force of a wing according to angle of attack
        
        Parameters
        ----------
        velocity : float
            relative velocity of the air on the wing 
        alpha : float
            angle on attack i.e. angle between air direction an wing chord (theta + i_w)
        rho : float [optional]
            air density in kg/m^3
        """
        CD=self.wingPerf.getParam(alpha, 'CD')
        D = CD *((rho*velocity**2)/2)*self.area
        return D  # fx_traînée_aile

    def getMoment(self, velocity, alpha, rho = 1.225, ti = 1.5):
        """
        function for the calculation of the moment of a wing and fuselage according to angle of attack
        
        Parameters
        ----------
        velocity : float
            relative velocity of the air on the wing 
        alpha : float
            angle on attack i.e. angle between air direction an wing chord (theta + i_w)
        rho : float [optional]
            air density in kg/m^3
        ti : float [optional]
        """
        CM=self.wingPerf.getParam(alpha, 'CM')
        M = CM *((rho*velocity**2)/2)*self.area * ti # TODO: correct this calculation
        return M  # Wing moment

class Foil:
    """
    Created on Thu Apr 20 21:45:42 2023
    @author: vujic


    This class allows you to calculate the aerodynamic forces and moments for 
    all types of foils

    Parameters
    ----------
    foilFile : text
        file with all coefficient depending of Re and alpha with
        this form : C:\direction\dolmen\direction\FileName.xlsx
    Span : float
        span of a blade [m]
    Roots_cord : float 
        Cord at roots (emplenture) [m]
    Tip_cord : float, optional if you have a rectangular foil
        The default is False.
        Cord at tip (bout de foil) [m]
        
    Fonctions
    -------
    getCord() #if you have a trapezoidal-shaped foil
    forces(alpha,u_inf,rho,Re)
    torque(alpha,u_inf, rho,Re)
    

    """
    def __init__(self,foilFile, Span, Roots_cord, Tip_cord=False):
        if Tip_cord==False:
            Tip_cord = Roots_cord
        self.Span = Span
        self.c = (Roots_cord+Tip_cord)/2
        self.S = self.c*self.Span
        self.foilFile = foilFile
    
    def getCord(self):
        return self.c
    
    def formFactor(self,alpha,Re):
        """
        This method comes from powerpoint 3 of the aerodynamics course

        Parameters
        ----------
        alpha : float
            attack angle [°]
        Re : float 
            Reynolds number[-]

        Returns
        -------
        Cl : float
            Lift  coefficient
        Cd : float 
            Drag coefficient of a finished foil
        Cm : float 
            Moment coefficient
        alpha_f : float
            reel attack angle [°]

        """
        self.Cl = tbl.dataFile.aeroCoef(Re,alpha,self.foilFile)[0]
        self.Cm = tbl.dataFile.aeroCoef(Re,alpha,self.foilFile)[2]
        AR = self.Span**2/self.S #-
        Of = (1.78*(1-(0.045*(AR**(0.68)))))-0.64 #Aircraft Design A Conceptual Approach by Daniel P. Raymer, Chapitre 12.6.1
        self.Cd = self.Cl**2/(math.pi*Of*AR)
        alpha_f = alpha + (self.Cl*180)/(math.pi**2*Of*AR)
        Cd = self.Cd
        Cl = self.Cl
        Cm = self.Cm
        return Cl, Cd, Cm, alpha_f

    def forces(self,alpha,u_inf,rho,Re):
        """
        Calculation of lift and drag forces

        Parameters
        ----------
        alpha : float
            attack angle [°]
        u_inf : float
            speed of the aircraft [m/s]
        rho : float
            Density of the fluid [kg/m^3]
        Re : float 
            Reynolds number[-]

        Returns
        -------
        Fd : float
            Drag [N]
        Fp : float
            Lift (p for portance) [N]

        """
        self.formFactor(alpha,Re)
        Fd = (self.Cd*rho*self.S*u_inf**2)/2
        self.Fp = (self.Cl*rho*self.S*u_inf**2)/2
        Fp = self.Fp
        return Fd, Fp

    def torque(self, alpha,u_inf, rho,Re):
        """
        Calculating the foil moment

        Parameters
        ----------
        alpha : float
            attack angle [°]
        u_inf : float
            speed of the aircraft [m/s]
        rho : float
            Density of the fluid [kg/m^3]
        Re : float 
            Reynolds number[-]

        Returns
        -------
        T : float
            Torque of the foil [Nm]

        """
        self.forces(alpha,u_inf, rho,Re)
        T = (self.Cm*rho*self.S*(u_inf**2)*self.c)/2
        return T


class Propeller:
    
    """
    
    Parameters
    ----------
    NbrBlades : int
        Number of blades
    D_hub : float
        Diameter of the hub (moyeu) [m]
    D_tip : float
        Diameter of the tip (Bout de pale) [m]
    Cord : float
        cord of the blade in the middle [m]
    Mass : float
        total mass of the propeller (with the hub) [kg]
    foilFile : text
        file with all coefficient depending of Re and alpha with
        this form : C:\direction\dolmen\direction\FileName.xlsx
    max_pitch : float
        the largest pitch that the propelle have (give it by the constructor) [m]
    wedgeAngle : float
        wedge angle of the blades
    Fixed_pitch : optional, booleen
        The default is False. Is your propeller with a fixed pitch? (True or False)
    open_prop : optional, booleen
        The default is True. Is your propelle shrouded (False) or open (True)?
    omega    : optional, Float
        The default is 0. The Initial rotation of the proppeler [rad/s]
                     this value will be saved by the class and incremented at each step
    prop_efficacity : float, optional
        The default is 0.7.
                    Efficacity of the propeller [-]
    Fonctions
    -------
    applyTorque (motorTorque, pitch_profile, u_inf, rho)
    calcOmega(prop_torque, t=1, h=0.02)
    getOmega()
    getThrust(u_inf, rho, Tw, pitch_profile)
    getTres(u_inf, pitch_profile, rho, TMotor)
    getAngular_acceleration(t, rot_velocity, prop_torque)
    
    """
    def __init__(self, NbrBlades, D_hub, D_tip, Cord, Mass, foilFile, max_pitch, wedgeAngle, Fixed_pitch = False, open_prop = True, omega = 0, prop_efficacity = 0.75):

        self.NbrBlades = NbrBlades
        self.D_hub = D_hub
        self.D_tip = D_tip
        self.Span = self.D_tip-self.D_hub
        self.Foil = Foil(foilFile, self.Span, Cord)
        self.x = (self.D_tip - self.D_hub)/2
        self.prop_efficacity = prop_efficacity
        InertiaMomentum = ia.getPropellerInertia(Mass,D_hub,D_tip,Cord,NbrBlades)
        self.Im = InertiaMomentum
        self.maxPitch = max_pitch
        self.Fixed_pitch = Fixed_pitch
        self.open_prop = open_prop
        self.DiscArea = ((self.D_tip**2)/4)*math.pi
        self.PropArea = self.DiscArea-((self.D_hub**2)/4)*math.pi
        self.sigma = self.PropArea/self.DiscArea
        self.cord = Cord
        self.wedgeAngle = wedgeAngle
        self.omega = omega
        
    def applyTorque(self, motorTorque, pitch_profile, u_inf, rho):
        """
        Apply the motor torque on the propeller inertia, causing acceleration / deceleration in relation with resistive torque 

        Parameters
        ----------
        motorTorque : float
            Torque received by motor on shaft.
        pitch_profile : float (or None)
            pitch control.
        u_inf : float
            relative speed of the propelle in the air.
        rho : float
            air density.

        Returns
        -------
        None.

        """
    
        self.Tres = self.getTres(u_inf, pitch_profile, rho)
        netto_torque = motorTorque - self.Tres
        self.Omega = self.calcOmega(netto_torque)
        self.current_uinf = u_inf
        self.currentPitch_profile = pitch_profile
        self.current_rho = rho

    def getTres(self, u_inf, pitch_profile, rho):
        """
        Calculate the resitive torque

        Parameters
        ----------
        u_inf : float 
            the trajectory speed of the aircraft
        pitch_profile : float or list
            pitch of the prop if fixed pitch : None [%]
        rho : float
            density of the fluid [kg/m^3]
        TMotor : float
            Torque given by the motor [Nm]

        Returns
        -------
        Tres : Float
            DESCRIPTION.Resistive Torque [Nm]

        """
        tangential_lin_speed = self.omega*self.x #[m/s]
        
        if tangential_lin_speed == 0:
            tangential_lin_speed = 0.00001
        
        real_angle = math.degrees(math.atan(u_inf/tangential_lin_speed))
        
        if self.Fixed_pitch == False:
            actualPitch = (pitch_profile*self.maxPitch)
            foil_angle = math.degrees(math.atan((actualPitch)/2.2))+self.wedgeAngle
        elif self.Fixed_pitch == True:
            actualPitch = self.maxPitch
            foil_angle = math.degrees(math.atan((actualPitch)/2.2))
        
        AttackAngles = foil_angle-real_angle
        
        u_inf = np.linalg.norm((u_inf, tangential_lin_speed))
        
        Re = fm.Adim.reynolds(self.cord, rho, fm.Air.visc, u_inf)
        
        Cl = self.Foil.formFactor(AttackAngles, Re)[0]
        Cd = self.Foil.formFactor(AttackAngles, Re)[1]

        AttackAngles = math.radians(AttackAngles)
        
        ftip = (self.NbrBlades/2)*((self.D_tip/2-self.x)/(self.x*math.sin(AttackAngles)))
        fhub = (self.NbrBlades/2)*((self.x-self.D_hub/2)/(self.x*math.sin(AttackAngles)))
        
        Fact = (2/math.pi*math.acos(math.exp(-(ftip*fhub))))
        a_ = (((4*Fact*math.sin(AttackAngles)*math.cos(AttackAngles))/(self.sigma*(Cl*math.sin(AttackAngles)-Cd*math.cos(AttackAngles))))+1)**(-1)
        
        if self.open_prop == True:
            tangentialForce = (rho*((((tangential_lin_speed*(1+2*a_))**2-tangential_lin_speed**2)*self.DiscArea)/2)*self.prop_efficacity)
        elif self.open_prop == False:
            tangentialForce = 1.3*(rho*((((tangential_lin_speed*(1+2*a_))**2-tangential_lin_speed**2)*self.DiscArea)/2)*self.prop_efficacity)
            
        Tres = tangentialForce * self.x/1000
        
        return Tres
    
    def getAngular_acceleration(self,t, rot_velocity, prop_torque):
        """
        Calculate the angular accelration in a fonction by RK4 used only to have the rot velocity at t+1

        Parameters
        ----------
        t : float 
            Integral step time [s]
        rot_velocity :  float
            T-1 rotation speed [rad/s]
        prop_torque : float
            Actual motor torque [Nm]

        Returns
        -------
        Angular_acceleration : float
            Angular acceleration of the propeller [rad/s^2]

        """
        Angular_accel = prop_torque/self.Im
        Angular_acceleration = np.array([Angular_accel])
        return Angular_acceleration
    
    def calcOmega(self, prop_torque, t=1, h=0.02):
        """
        Calculation of rotational speed via angular acceleration

        Parameters
        ----------
        prop_torque : float
            Actual motor torque [Nm]
            
        t : optional, float
            The default is 1. Integral step time [s]
            
        h : optional Float
            The default is 0.02. Increment of the integral [s]

        Returns
        -------
        newOmega : float
            The actual rotation speed of the propeller [rad/s]

        """
        newOmega = pyi.run_kut4(self.omega, lambda t, x: self.getAngular_acceleration(t, x, prop_torque), t, h)
        
        self.omega = newOmega
        return newOmega
    
    def getOmega(self):
        return self.omega
    
    def getThrust(self):
        """
        calculating the thrust of propellers
        Function 'applyTorque()' has to be run before to call this one.

        Parameters
        ----------
        u_inf : float
            speed of the aircraft [m/s]
        rho : float
            Density of the fluid [kg/m^3]
        pitch_profile : float
            Variation of the pitch over time (for variable pitches) [m] 

        Returns
        -------
        Thrust : float
            Thrust of the propeller [N]

        """
        
        u_inf = self.current_uinf
        rho = self.current_rho
        tangential_lin_speed = self.Omega*self.x #[m/s]

        if tangential_lin_speed == 0:
            tangential_lin_speed = 0.00001

        real_angle = math.degrees(math.atan(u_inf/tangential_lin_speed))
        
        if self.Fixed_pitch == False:
            actualPitch = (pitch_profile*self.maxPitch)
            foil_angle = math.degrees(math.atan((actualPitch)/2.2))+self.wedgeAngle
        elif self.Fixed_pitch == True:
            actualPitch = self.maxPitch
            foil_angle = math.degrees(math.atan((actualPitch)/2.2))
        
        AttackAngles = foil_angle-real_angle
        
        u_inf = np.linalg.norm((u_inf, tangential_lin_speed))
        
        Re = fm.Adim.reynolds(self.cord, rho, fm.Air.visc, u_inf)
        
        Cl = self.Foil.formFactor(AttackAngles, Re)[0]
        Cd = self.Foil.formFactor(AttackAngles, Re)[1]
        AttackAngles = math.radians(AttackAngles)
        
        ftip = (self.NbrBlades/2)*((self.D_tip/2-self.x)/(self.x*math.sin(AttackAngles)))
        fhub = (self.NbrBlades/2)*((self.x-self.D_hub/2)/(self.x*math.sin(AttackAngles)))
        
        Fact = (2/math.pi*math.acos(math.exp(-(ftip*fhub))))
        
        a = (((4*Fact*math.sin(AttackAngles)**2)/(self.sigma*(Cl*math.cos(AttackAngles)-Cd*math.sin(AttackAngles))))-1)**(-1)
        
        if self.open_prop == True:
            Thrust = (rho*((((u_inf*(1+2*a))**2-u_inf**2)*self.DiscArea)/2)*self.prop_efficacity)
        elif self.open_prop == False:
            Thrust = 1.3*(rho*((((u_inf*(1+2*a))**2-u_inf**2)*self.DiscArea)/2)*self.prop_efficacity)
        
        return Thrust
        
class Fuselage:
        """
        This class lets you calculate the fuselage's drag force.

        Parameters
        ----------
        diamFuse : float
            Diameter of the fuselage [m]
        lFuse : float
            lenght of the plane. [m]

        Fonction
        -------
        formFactor(rho, Mach, u_inf)
        dragFuse(rho, Mach, u_inf)

        """
        def __init__(self, diamFuse,lFuse):
            self.diamFuse=diamFuse
            self.lFuse=lFuse
            self.sFront = math.pi*(diamFuse/2)**2
            self.sWet = math.pi*diamFuse*lFuse
            self.FR = self.lFuse/self.diamFuse

        
        def formFactor(self,rho, Mach,u_inf):
            """
            Calcul the aerodynamic drag coefficient

            Parameters
            ----------
            rho : float
                Density of the fluid [kg/m^3]
            Mach : float
                Mach number [-]
            u_inf : float
                speed of the aircraft [m/s]

            Returns
            -------
            CdFuse : flat
                Drag coefficient of the fuselage
            """

            Re = fm.Adim.reynolds(self.lFuse, rho, fm.Air.visc, u_inf)
            Cdfp = 0.455/((math.log10(Re)**2.58)*(1+0.144*Mach**2)**0.65)
            Cf = (Cdfp * ((0.0235*self.FR*Re**(-0.2))+(self.FR)**(-1.5)+(7*(self.FR)**(-3)))+ Cdfp)*1.025
            CdFuse = Cf*(self.sWet/self.sFront)
            return CdFuse
        
        def dragFuse(self,rho,Mach,u_inf):
            """
            This function calculates fuselage drag

            Parameters
            ----------
            Re : float
                Reynolds number [-]
            Mach : float
                Mach number [-]
            diamFuse : float
                Diameter of the fuselage [m]

            Returns
            -------
            Fd : float
                fuselage drag [N]

            """
            Cd = self.formFactor(rho,Mach,u_inf)
            Fd = (Cd*rho*self.sWet*u_inf**2)/2
            return Fd
            
if __name__ == "__main__":
    import DataSet as data
    
    prop = Propeller(data.Nblades, data.DHub, data.Dtip, data.Cord, data.Mass, data.PropFile,data.PropPitch, data.WedgeAngleProp, True,False)     
    
    self.Tres = prop.getTres(0, False, 1.3, 17)
    
    thrust = prop.getThrust(763, 1.3, -0.2, None)
    
    print('\n', 'Tres:',Tres,'Nm','\n', 'thrust:',thrust,'N')