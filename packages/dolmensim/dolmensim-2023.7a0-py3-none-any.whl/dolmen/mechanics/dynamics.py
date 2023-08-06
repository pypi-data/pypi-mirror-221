# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:34:09 2022

@author: nicolas.rouve
"""

class Gravity:
    M=5.9742*1e24 #kg
    G=6.6738*1e-11 #(N*m^2)/kg^2
    R=6371030 #m
        
    def accel(z):
        """
        Gives the gravitational acceleration as a function of altitude
        
        Parameters
        ----------
        z : TYPE float
            DESCRIPTION. altitude [m]

        Returns
        -------
        g : TYPE float
            DESCRIPTION. gravitational acceleration [m/s^2]

        """
        g=(Gravity.G*Gravity.M) / (Gravity.R+z)**2
        return g
    
    def gravity(h=0):
        return Gravity.accel(h)

class Newton:
    """
    Each moving mass shall be instanciated separately
    Args: mass (kg)
    """
    def __init__(self, m):
        self.m = m
        if m == 0 : print('dynamics::Newton > error: mass cannot be null')
        
    # def getForce(self,accel):
    #     force = self.m*accel  
    #     return force
    
    def getAcceleration(self,force):
        """
        Args: [position (m), speed(m/s)]
        Out : [speed(m/s), acceleration (m/s^2)]
        """
        acceleration = force / self.m 
        return acceleration

if __name__ == '__main__':
    z = 0
    Gravity = Gravity()
    print(f"gravity at {z} m : {round(Gravity.accel(z),4)}")
    z = 1e3
    print(f"gravity at {z} m : {round(Gravity.accel(z),4)}")
    z = 5e3
    print(f"gravity at {z} m : {round(Gravity.accel(z),4)}")
    z = 20e3
    print(f"gravity at {z} m : {round(Gravity.accel(z),4)}")
    