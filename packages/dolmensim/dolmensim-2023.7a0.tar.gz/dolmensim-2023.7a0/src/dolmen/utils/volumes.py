# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:31:58 2023

@author: vujic

Basic volume calculation
"""

import math

def cube(a):
    V=a**3
    return V

def emptyCube(a_ext, a_int = None, e= None):
    if a_int != None:
        V= cube(a_ext)- cube(a_int)
    elif e != None:
        a_int = a_ext-e
        V= cube(a_ext)- cube(a_int)
    else :
        raise ValueError("Give a value of either r_int or e")
    return V

def rectangular_parallelepiped(a,b,c):
    V=a*b*c
    return V

def emptyRectangular_parallelepiped(a,b,c,e):
    V= rectangular_parallelepiped(a,b,c) - rectangular_parallelepiped(a-e, b-e, c-e)
    return V

def sphere(r):
    V=(4/3)*math.pi*r**3
    return V

def emptySphere(r_ext, r_int=None, e=None):
    if r_int != None:
        V= sphere(r_ext)- sphere(r_int)
    elif e != None:
        r_int = r_ext-e
        V= sphere(r_ext)- sphere(r_int)
    else :
        raise ValueError("Give a value of either r_int or e")
    return V 

def cylinder(r,l):
    V = math.pi*r**2*l
    return V

def tube(r_ext, l, r_int = None, e = None):
    if r_int != None:
        V= cylinder(r_ext, l)- cylinder(r_int, l)
    elif e != None:
        r_int = r_ext-e
        V= cylinder(r_ext, l)- cylinder(r_int, l)
    else :
        raise ValueError("Give a value of either r_int or e")
    return V

def propeller(Dhub, Dtip, cord, e, NbrBlades):
    """dolmen\_howTo\Traînée d'un fuselage.docx"""
    Vblades = NbrBlades * rectangular_parallelepiped(cord, (Dtip-Dhub), e)
    V = cylinder(Dhub,e)+Vblades
    return V