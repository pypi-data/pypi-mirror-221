# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:39:55 2022

@author: nicolas.rouve
"""
import math
import numpy as np

class Totalizer:
    """
    a class used to totalize quantities like energy, volume, charge, aso.
    TODO :
        - establish where the time comes from
    """
    def __init__(self):
        self.tot = 0.0
        self.lastT = 0.0
        
    def add(self, delta):
        """ Add a value to the totalizer, for example Joules in an energy totaliser """
        self.tot += delta
        
    def getTot(self):
        return self.tot

    def integrate(self, rate, t):
        """ Add a time multiplicated value to the totalizer, for example Watt in an energy totaliser """
        h = t-self.lastT
        self.tot += rate * h
        self.lastT = t

def cart2pol(x,y):
    """
    converts cartesian in polar coordinates in DEGREES
    returns rho, phi
    """
    rho = math.sqrt(x**2 + y**2)    
    phi = math.degrees(math.atan(y/x)) if x!=0 else 90 if y!=0 else 0
    if x<0 and y>0 : phi +=180 # 2nd quadrant
    if x<0 and y<0 : phi -=180 # 3rd quadrant
    return rho, phi

def pol2cart(rho, phi):
    """
    converts polar (in DEGREES) in cartesian coordinates
    """
    x = rho * math.cos(math.radians(phi))
    y = rho * math.sin(math.radians(phi))
    return x,y

def cart2spher(x,y,z):
    """
    Selon le CRM p.67 edition 2018
    x = 0° trigonomètrique
    """
    
    rho = math.sqrt(x**2 + y**2 + z**2)
    phi = math.degrees(math.atan(y/z)) #between x and y axis
    theta = math.degrees(math.asin(z/rho))  #Between the plane xy and the axe z
    
    if x<0 and y>0 : phi +=180 # 2nd quadrant
    if x<0 and y<0 : phi -=180 # 3rd quadrant
    
    return rho, phi, theta

def spher2cart(rho, phi, theta):
    x = rho*math.cos(math.radians(theta))*math.cos(math.radians(phi))
    y = rho*math.cos(math.radians(theta))*math.sin(math.radians(phi))
    z = rho*math.sin(math.radians(theta))
    
    return x, y, z
    

def vectProject(u_toProject, v_reference):
    """
    projects a vector on an other
    https://fr.acervolima.com/projection-vectorielle-a-laide-de-python/
    """
    v_norm = np.sqrt(sum(v_reference**2))     
    proj_of_u_on_v = (np.dot(u_toProject, v_reference)/v_norm**2)*v_reference
    return proj_of_u_on_v

if __name__ == "__main__":
    print ('4 quadrants:')
    print ("x=8.5, y= 5 -> rho, phi =",cart2pol(8.6,5))
    print ("x=-8.6, y= 5 -> rho, phi =",cart2pol(-8.6,5))
    print ("x=-8.6, y= -5 -> rho, phi =",cart2pol(-8.6,-5))
    print ("x=8.6, y= -5 -> rho, phi =",cart2pol(8.6,-5))
    print ('horiz/vert')
    print ("x=10, y= 0 -> rho, phi =",cart2pol(10,0))
    print ("x=0, y= 5 -> rho, phi =",cart2pol(0,5))
    print ()
    print ("rho = 14.14, phi = 45 -> x,y =", pol2cart(14.14, 45))
    print ("rho = 25, phi = 90 -> x,y =", pol2cart(25, 90))
    print ('4 quadrants:')
    print ("rho = 10, phi = 30 -> x,y =", pol2cart(10, 30))
    print ("rho = 10, phi = 150 -> x,y =", pol2cart(10, 150))
    print ("rho = 10, phi = -150 -> x,y =", pol2cart(10, -150))
    print ("rho = 10, phi = -30 -> x,y =", pol2cart(10, -30))
    print ('more than half turn')
    print ("rho = 10, phi = 330 -> x,y =", pol2cart(10, 330))
    print ("rho = 10, phi = 390 -> x,y =", pol2cart(10, 390))
    print ("vect proj")
    print (vectProject(np.array([1,2,3]), np.array([5,6,2])))