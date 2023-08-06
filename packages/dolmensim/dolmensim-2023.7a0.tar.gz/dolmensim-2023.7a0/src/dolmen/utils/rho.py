# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:08:36 2023

@author: vujic

This file contains the densities of different materials and allows you 
to calculate alloy density.
Data in [kg/m^3]
dolmen\_howTo\Traînée d'un fuselage.docx
"""

import numpy as np

def alloy(rho_array, proportion_array):
    """
    Calcul the density of your alloy

    Parameters
    ----------
    rho_array : TYPE numpy.ndarray
        DESCRIPTION. alloy density composition each i must be in [kg/m^3]
    proportion_array : TYPE numpy.ndarray
        DESCRIPTION. alloy density composition (please don't write 10% but 0.1)
                                                
    all rho values will have a correspondence with a proportion, make sure you put each i in the same position
    Returns
    
    -------
    rho_alloy : TYPE float
        DESCRIPTION. the density of your alloy[kg/m^3]

    """
    if np.sum(proportion_array) >1:
        raise ValueError("Be careful, your alloy percentage is too high or the percentages have not been noted in 0.XXX.")
    elif np.sum(proportion_array)<1:
        raise ValueError("Be careful, your alloy percentage is too low")
    rho_alloy = np.array([])
    i=0
    for i in range(len(rho_array)):
        rho_i = rho_array[i]*proportion_array[i]
        rho_alloy = np.append(rho_alloy, rho_i)
    
    rho_alloy = np.sum(rho_alloy)
    
    return rho_alloy

#------------------------------------------------------------------------------
"Data from CRM"
Steel = 7850
Aluminium = 2700
Alu = 2700
Epoxy = 1200
Silver = 10500
Oak = (600+750)/2
Ebony = (1100-1330)/2
Spurce = (440+470)/2
Carbon = 2250
Chrome = 7190
Copper = 8960
Iron = 6890.0
Cork = (120+260)/2
Magnesium = 1740
Manganese = 7300
Grey_cast_iron = 7200
Nylon = 1140
Gold = 19300
Lead = 11300
Polyethylene = 930
PE = 930
Polypropylene = 910
PP = 910
Polyurethane = (350+650)/2
PU = (350+650)/2
Polystyrene = 1050
EPS = 1050
PVC = 1380 #https://fr.wikipedia.org/wiki/Polychlorure_de_vinyle
Sagex = 20
Titanium = 4560
Glass = 1180
Pyrex = 2320
Tungsten = 19300
Zinc = 7130
Tin = 7287


