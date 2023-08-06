# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:30:08 2022

@author: nicolas.rouve

# https://python.plainenglish.io/reference-frame-transformations-in-python-with-numpy-and-matplotlib-6adeb901e0b0
"""

import numpy as np


# # rotation of phi is about the 1st axis (=X-axis) of the inertial frame
# def r1(phi):
#     return np.array([[1, 0, 0],
#                      [0, np.cos(phi), np.sin(phi)],
#                      [0, -np.sin(phi), np.cos(phi)]])


# # second rotation of theta is about the 2nd axis (=Y-axis) of the first intermediate frame
# def r2(theta):
#     return np.array([[np.cos(theta), 0, -np.sin(theta)],
#                      [0, 1, 0],
#                      [np.sin(theta), 0, np.cos(theta)]])


# # third rotation of psi is about the 3rd axis (=Z-axis) of the second intermediate frame
# def r3(psi):
#     return np.array([[np.cos(psi), np.sin(psi), 0],
#                      [-np.sin(psi), np.cos(psi), 0],
#                      [0, 0, 1]])

# ====================================================
# e123 rotation sequence

d2r = np.pi/180
r2d = 1/d2r

def q11(psi, theta):
    return np.cos(psi) * np.cos(theta)


def q12(psi, theta, phi):
    return np.cos(psi) * np.sin(theta) * np.sin(phi) + np.sin(psi) * np.cos(phi)


def q13(psi, theta, phi):
    return -np.cos(psi) * np.sin(theta) * np.cos(phi) + np.sin(psi) * np.sin(phi)


def q21(psi, theta):
    return - np.sin(psi) * np.cos(theta)


def q22(psi, theta, phi):
    return -np.sin(psi) * np.sin(theta) * np.sin(phi) + np.cos(psi) * np.cos(phi)


def q23(psi, theta, phi):
    return np.sin(psi) * np.sin(theta) * np.cos(phi) + np.cos(psi) * np.sin(phi)


def q31(theta):
    return np.sin(theta)


def q32(theta, phi):
    return - np.cos(theta) * np.sin(phi)


def q33(theta, phi):
    return np.cos(theta) * np.cos(phi)


def e123_dcm(psi, theta, phi):
    """
    returns the Direct Cosine Matrix for a psi-theta-phi rotation
    Angles given in DEGREES !
    """
    psi, theta, phi = d2r*psi, d2r*theta, d2r*phi
    return np.array([[q11(psi, theta), q12(psi, theta, phi), q13(psi, theta, phi)],
                     [q21(psi, theta), q22(psi, theta, phi), q23(psi, theta, phi)],
                     [q31(theta),      q32(theta, phi),      q33(theta, phi)]])
    # TODO : verify if rotation is correct for aviation : usually E321 (psi, theta, phi, ie yaw, pitch, roll)


# def degrees2DCM(phy, theta, psi):
#     """
#     returns the DCM for three angles (in degrees) in a E123 sequence
#     Parameters
#     ----------
#     phi, theta, psi : float
#         the three rotation angles (roll, pitch, yaw
#     """
    # r1 = np.array([
    #     [1,     0,           0],
    #     [0,  np.cos(phi), np.sin(phi)],
    #     [0, -np.sin(phi), np.cos(phi)]])

    # r2 = np.array([
    #     [np.cos(theta), 0, -np.sin(theta)],
    #     [   0,          1,     0],
    #     [np.sin(theta), 0,  np.cos(theta)]])
    
    # r3=np.array([
    #     [ np.cos(psi), np.sin(phi), 0],
    #     [-np.sin(psi), np.cos(psi), 0],
    #     [    0,           0,        1]])
 

def getVector(orig, DCM):
    """
    returns the given vector in a new frame, given by DCM
    Parameters
    ----------
    orig : np.array[3]
        vector in actual frame
        
    DCM : np.array [3,3]
        Direction Cosine Matrix
    """
    destVect = np.dot(DCM, orig)
    return destVect

# def vector2degrees(vector):
    """
    https://stackoverflow.com/questions/21622956/how-to-convert-direction-vector-to-euler-angles
    
    returns the three angles phi, theta, psi of the given vector, in degrees

    parameters
    ----------
    vector : np.array
        contains 3 coordinates x, y, z of a vector
    
    Returns
    -------
        tuple : the three angles (E123) phi, theta, psi 
        
    """
    # x, y, z = vector
    # # angles in 1st quadrant
    # psi = r2d * np.arctan2(y, x)
    # l = np.linalg.norm(vector)
    # theta = r2d * np.arcsin(z/l)
    # phi = 0 # todo !!5
    # # TODO
    # # angles in all quadrants
    # return (phi, theta, psi)


if __name__ == '__main__':
    o = np.array([25, 0, 0])
    print ("o = ", o)
    phi   = 0
    theta = 15
    psi   = 0
    dcm   = e123_dcm(psi, theta, phi)
    print ("dcm=\n", dcm)
    d = getVector(o, dcm)
    print ('d=\n', d)
    print ("d'=\n", getVector(d, dcm.T))
    print()
    
    o = np.array([-1478.4, 0, -260.7])
    print ("SumForcesFrmPln = ", o)
    phi   = 0
    theta = 10
    psi   = 0
    dcm   = e123_dcm(psi, theta, phi)
    print ("dcm=\n", dcm)
    d = getVector(o, dcm.T)
    print ("SumForcesFrmGnd = ", d)
    print()
    
    o = np.array([-2.5, 0, -0.4])
    print ("accelFrmPln = ", o)
    phi   = 0
    theta = 10
    psi   = 0
    dcm   = e123_dcm(psi, theta, phi)
    print ("dcm=\n", dcm)
    d = getVector(o, dcm.T)
    print ('accelFrmGnd = ', d)
    # phi, theta, psi = vector2degrees(d)
    # print (phi, theta, psi)
