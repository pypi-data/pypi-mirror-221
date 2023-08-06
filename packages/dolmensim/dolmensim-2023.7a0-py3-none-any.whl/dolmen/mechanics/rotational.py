# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:04:22 2022

@author: nicolas.rouve
"""
import sys

class Reducer :
    """
    mechanical reducer, to be mounted on a rotating shaft
    - i = reduction ratio
    - efficiency = energy transfer ratio ($\eta$)
    """
    
    def __init__(self, i, efficiency = 1.0):
        self.i = i
        self.efficiency = efficiency
        if i == 0 : sys.exit('rotational::Reducer > error: reduction ratio cannot be null')
        if efficiency == 0 : sys.exit('rotational::Reducer > error: efficiency ratio cannot be null')

    def getOutTorque(self, inTorque):
        outTorque = inTorque * self.i * self.efficiency
        return outTorque
    
    def getInTorque(self, outTorque):
        inTorque = outTorque / self.i / self.efficiency
        return inTorque

    def getOutSpeed(self, inSpeed):
        outSpeed = inSpeed / self.i
        return outSpeed

    def getInSpeed(self, outSpeed):
        inSpeed = outSpeed * self.i
        return inSpeed

class Wheel:
    """
    mechanical wheel, convert linear to rotational and vice-versa,
    for velocita and Force/Torque
    - r = radius (half diameter ;-)
    """
    def __init__(self, r):
        self.r = r
        if r == 0 : sys.exit('rotational::Wheel> error: Wheel radius cannot be null')
        
    def getLinVel(self, rotVel):
        linVel = rotVel*self.r
        return linVel
    
    def getRrotVel(self, linVel):
        rotVel = linVel/self.r
        return rotVel
        
    def getForce(self, torque):
        force = torque/self.r
        return force

    def getTorque(self, force):
        torque = force * self.r
        return torque
        
    def getTorque(self, force):
        torque = force * self.r
        return torque
        
if __name__ == "__main__":
    redToto = Reducer(50,0.9)
    outTorque = 2000
    inTorque = redToto.getInTorque(outTorque)
    print (f">>reducer : inTorque={inTorque}, outTorque={outTorque}")