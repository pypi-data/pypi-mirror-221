# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:39:25 2022

@author: nicolas.rouve
"""
import sys

class Torquemotor:
    # simple T=Kt*i motor
    
    def __init__(self, Kt):
        # init with Kt coef (N*m/A)
        self.Kt = Kt
        if Kt == 0 : sys.exit('Motors::TorqueMotor > error: Torque constant cannot be null')

    def getTorque(self, current):
        # generated torque is proportionnal to current
        generatedTorque = self.Kt * current
        return generatedTorque

class Motor:
    def __init__(self, T_nom,w_nom,w_max,p_nom):
        self.T_nom = T_nom
        self.w_nom = w_nom
        self.w_max = w_max
        self.p_nom = p_nom
    
    def getMaxTorque(self, v_mot):
        ''' Fonction de calcul du couple moteur générique max d'un moteur typique BLDC
            en fonction de sa vitesse de rotation
            return T_motor
        écrit par V Bourquin, 2020 04 24 - 02:51
        '''
        # Couple moteur en fonction de la vitesse de rotation du moteur
        if v_mot <= self.w_nom:
            T_motor = self.T_nom
        elif v_mot <= self.w_max:
            T_motor = self.p_nom / v_mot
        else:
            T_motor = 0
        return T_motor
