# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:46:59 2023

@author: vujic
"""

"""
This file is used to calculate values useful for fluid mechanics
"""
import numpy as np

class Air:
    def density(z):
        """
        air density as a function of altitude

        Parameters
        ----------
        z : TYPE float
            DESCRIPTION. altitude [m]

        Returns
        -------
        rho : TYPE float
            DESCRIPTION. density [kg/m^3]

        """
        a=1.247015
        b=0.000104
        rho=a*np.exp(-b*z) #https://wind-data.ch/tools/luftdichte.php?lng=fr
        return rho
    
    visc = 1.81*10e-5
    
class Adim:
        """
        Reynolds(c,rho,visc,u_inf)
        mach(u_inf, altitude)
        
        """
    
        def reynolds(c, rho, visc, u_inf):
            """
            Calculating the reynolds number

            Parameters
            ----------
            c : TYPE float
                DESCRIPTION. for plane : cord [m]
                             for other form : flow length [m]
            rho : TYPE float
                DESCRIPTION. Density of the fluid [kg/m^3]
            visc : TYPE  float
                DESCRIPTION. dynamic viscosity
                            Air(20°C) = 1.81e-5 [Pa*s]
                            Water(20°C) = 1e-3 [Pa*s]
            u_inf : TYPE float
                DESCRIPTION. speed of the fluid parallel to the flow length [m/s] 

            Returns
            -------
            Re : TYPE float
                DESCRIPTION. Reynolds Number [-]
            """
            Re = (u_inf * c * rho) / visc
            return Re
        
        def mach(u_inf, altitude):
            """
            Allows you to calculate the number of mach to know if you have
            exceeded the sound barrier or not. Taking into account the variation
            of temperature with altitude. 
            https://fr.wikipedia.org/wiki/Nombre_de_Mach#:~:text=Le%20nombre%20de%20Mach%20est,son%20dans%20ce%20m%C3%AAme%20fluide.

            Parameters
            ----------
            u_inf : TYPE float
                DESCRIPTION. peed of the fluid parallel to the flow length [m/s]
            altitude : TYPE float
                DESCRIPTION. altitude [m]

            Returns
            -------
            MachNum : TYPE float
                DESCRIPTION. Mach Number

            """
            if altitude < 500:
                a = 340.3
            elif 500 <= altitude <1165:
                a = 336.4
            elif 1165<= altitude <3650:
                a = 331.3
            elif 3560<= altitude < 6250:
                a = 320.5
            elif 5250 <= altitude < 9250:
                a = 310.2
            elif 9250<= altitude < 26000:
                a = 295.1
            elif 26000 <= altitude < 39500:
                a = 303.1
            else: a = 329.8
            
            MachNum = u_inf/a
            
            return MachNum
        
class FluidsForces:
    def __init__(self, rho):
        self.rho = rho
        
    def archimedes(self,V,g):
        ArchiForce = V*g*self.rho
        return ArchiForce