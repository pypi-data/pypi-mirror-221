# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:48:25 2022

@author: nicolas.rouve
copied from C:/Users/nicolas.rouve/Documents/20_PROJETS/PYTHON/Control/LTI
developed in march 2020
"""

import dolmen.control.LTIsystem as lti

class PID (lti.LTI):
    """
    This class lets you define and slave values

    Parameters
    ----------
    Kp : TYPE, optional float
        DESCRIPTION. The default is 0.1. The proportional factor [-]
    Ti : TYPE, optional floatr
        DESCRIPTION. The default is 0. The integral factor [-]
    Td : TYPE, optional float
        DESCRIPTION. The default is 0. The derivat factor [-]
    MaxValue : TYPE, optional float
        DESCRIPTION. The default value is 100, because by default the return is given as a percentage.
        But you can choose the output units and set the maximum value.
    MinValue : TYPE, optional float
        DESCRIPTION. The default value is -100, because by default the return is given as a percentage.
        But you can choose the output units and set the minimum value.
    Fonction
    -------
    compute (w, y, t)

    """ 
    def __init__ (self, Kp = 0.1, Ti = 0, Td = 0, MaxValue = 100, MinValue=-100):
        lti.LTI.__init__(self)
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.ei = 0 # error integral
        self.last_e = 0
        self.MaxValue = MaxValue
        self.MinValue = MinValue
        # self.errorFilter   = lti.system([0,1],[.1,1])
        # print('PID initialized.')
  
    def compute (self, w, y, t):
        """
        Calcul the output value

        Parameters
        ----------
        w : TYPE float
            DESCRIPTION. Desired input value [you know]
        y : TYPE float
            DESCRIPTION. Actual input value [you know]
        t : TYPE float
            DESCRIPTION. step time [s]

        Returns
        -------
        u : TYPE
            DESCRIPTION.

        """
        # print('starting PID::compute :', 'w=', w, 'y=',y)
        self.measurePeriod (t) # call function from parent class to get exec time

        #init
        ui = ei = ed = ud = 0
        # compute the error
        e = w - y
        # e = self.errorFilter.compute(e, t)

        # compute the proportional component
        up = self.Kp * e
        # print(up)
        
        # compute the integral component (with anti-wind-up)
        if self.Ti <= 0 : ui = 0
        else :
            ei = self.ei + e * self.h # compute error integral (sum !)
            ui = self.Kp / self.Ti * ei
        # print (ui)

        # compute the derivative component
        if self.Td <= 0 : ud = 0
        else :
            if self.h > 0 :
                ed = (e - self.last_e) / self.h #compute error derivative
            else:
                ed = 0
            ud = self.Kp * self.Td * ed
        # print (ud)
        
        self.last_e = e # store value for next cycle
        
        u = up + ui + ud
        # print (u)
        if self.Ti > 0 :
            if self.MinValue < u < self.MaxValue :    # ok, no wind-up
                self.ei = ei        # keep new intregral 

        if   u < self.MinValue : u = self.MinValue # if signal out of bounds
        elif u > self.MaxValue : u = self.MaxValue # limit output
        
        # print ('e={:.2f}\t up={:.2f}\t ei={:.2f}\t ui={:.2f}\t ed={:.2f}\t ud={:.2f}\t u={:.2f}\t '.format(e, up, ei, ui, ed, ud, u))#, end='')   
        
        return u


if __name__ == "__main__" :
    import numpy as np
    import matplotlib.pyplot as plt
    w = 10
    y = 0 
    Y=[]
    T=[]
    corr_y = PID(1, 0, 0)
    for t in range(100):
        u = corr_y.compute(w, y)
        y += u/10
        print (y)
        Y.append(y)
        T.append(t)
    arr_y = np.array(Y)
    arr_t = np.array(T)
    
    plt.plot(arr_t, arr_y)