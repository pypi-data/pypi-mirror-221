# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:14:17 2022

@author: nicolas.rouve
TODO : implement a 3d version 
        - set coordinates of the base (6 DOF)
        - get inertia vector relative to the base or to another point
"""

import numpy as np

def getPointMassInertia (m, r): return m * np.linalg.norm(r**2)

def getTrapezoidInertia(m, h, base, top, r=0):
    """
    returns the inertia along diametral axis
    """
    
    ownInertia = (h**3)*(base**4 - top**4)/(48*m**2*(base - top)) # To Be verified, unique source is Code from VL...
    return ownInertia + getPointMassInertia(m, r)

def getEmptyCylinderInertiaLong(m, ri, re, h, r=0):
    """
    returns the inertia along longitudinal axis
    https://www.123calculus.com/inertie-cylindre-creux-page-8-95-120.html
    """
    ownInertia = 1/2 * m *(ri**2 + re**2)
    return ownInertia + getPointMassInertia(m, r)

def getEmptyCylinderInertiaDiam(m, ri, re, h, r=0):
    """
    returns the inertia along diametral axis
    https://www.123calculus.com/inertie-cylindre-creux-page-8-95-120.html
    """
    ownInertia = 1/12 * m *(3* (ri**2 + re**2) + h**2)
    return ownInertia + getPointMassInertia(m, r)

def getEmptyConeInertiaLong(m, ri, re, h, r=0):
    """
    returns the inertia along longitudinal axis
    """
    ownInertia = 1/2 * m # .......
    return ownInertia + getPointMassInertia(m, r)

def getEmptyConeInertiaDiam(m, ri, re, h, r=0):
    """
    returns the inertia along diametral axis
    """
    ownInertia = 1/20 * m *(3* r**2 + 2* h**2) # To Be verified, unique source is Code from VL...
    return ownInertia + getPointMassInertia(m, r)

def getParallelepipedInertia(m, a, b, r=0):
    """
    returns the inertia
    """
    ownInertia = 1/12 * m *(a**2 + b**2)
    return ownInertia + getPointMassInertia(m, r)
    
def getPropellerInertia(PropellerMass, Dhub, Dtip, cord, NbrBlades=2):
    """
    You can find the devlopper of this calculation on "dolmen\_howTo\Moment d'inertie.docx"
    
    Parameters
    ----------
    PropellerMass : TYPE float
        DESCRIPTION. Total mass of the propeller [kg]
    Dhub : TYPE float
        DESCRIPTION. Diameter of the hub [m]
    Dtip : TYPE float
        DESCRIPTION. diameter of the propeller [m]
    cord : TYPE float
        DESCRIPTION. Cord at the tip [m]
    NbrBlades : TYPE, optional, int
        DESCRIPTION. The default is 2.
                    Nbr of blades

    Returns
    -------
    ownInertia : TYPE
        DESCRIPTION.

    """
    rc = Dhub/2
    rp = Dtip/2
    mc = 2/3 * PropellerMass
    mp = (1/3 * PropellerMass)/NbrBlades
    a = rp - rc
    J1Foil = mp * (a**2+cord**2)/12
    l = rc+a/2
    ownInertia = mc/2 * rc**2 + NbrBlades*(J1Foil+ (mp * l**2)) #[kg*m^2]
    return ownInertia