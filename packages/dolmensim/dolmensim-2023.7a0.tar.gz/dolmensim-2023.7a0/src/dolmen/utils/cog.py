# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 13:44:17 2023

@author: vujic

This program finds the center of gravity of a set of objects with the following
calcul:
r ⃗_o = (1/(∑i m_i))∗ ∑im_i∗ r ⃗_i = (1/(∑i〖ρ_i∗V_i〗))∗∑i〖ρ_i∗V_i〗∗ r ⃗_i
"""

def COG(massElements, volumeElements=None):
    """
    This program calculates the center of gravity of a set. To do this, 
    you need to give the function a mass array containing lists, each list 
    containing information about one element of the set. It may be that the 
    mass is not known, in which case the volume and density can be given to
    perform the same calculation. Here's what lists in arrays should look like:



    Parameters
    ----------
    massElements : TYPE numpy.nparray
        DESCRIPTION. array filled with information list by mass elements
             Element mass: [array of center of gravity, element mass].
    volumeElements : TYPE, optional, TYPE numpy.nparray
        DESCRIPTION. array filled with information list by volume elements
             Element volume: [array of center of gravity, element volume, element density].

    Returns
    -------
    COG : TYPE numpy.nparray
        DESCRIPTION. center gravity of the set

    """
    massm = []
    massv = []
    cgm = []
    volume = []
    rho = []
    cgv = []
    
    for i in range(len(massElements)):
        cgm.append(massElements[i][0])
        massm.append(massElements[i][1])

    if volumeElements is not None:
        for j in range(len(volumeElements)):
            cgv.append(volumeElements[j][0])
            volume.append(volumeElements[j][1])
            rho.append(volumeElements[j][2])
        massv = [v * r for v, r in zip(volume, rho)]
        mass = massm + massv
        cg = cgm + cgv
    else:
        mass = massm
        cg = cgm
        
    totmass = sum(mass)
    COG = sum([(m * c) / totmass for m, c in zip(mass, cg)])

    return COG