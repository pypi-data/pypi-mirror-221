# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:55:35 2022

@author: nicolas.rouve
"""

class Tire:
    """
    a class used to simulate the contact of a tire on the ground
    
    Attibutes
    ---------
    c_rollRes : float
        rolling resistance coefficient
    """
    def __init__(self, c_rollRes = 0):
        self.c_rollRes = c_rollRes
        

    def getRollRes(self, reaction):
        """
        gives the force opposed to the movement, proportionnally to the reaction of the ground on the plane

        Parameters
        ----------
        reaction: float
            force applied between tire and ground (N)
            
        """
        F_rollRes = reaction*self.c_rollRes
        return F_rollRes
