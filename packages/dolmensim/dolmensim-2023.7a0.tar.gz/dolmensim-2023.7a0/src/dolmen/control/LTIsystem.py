# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:33:07 2020

         Y(s)      [[b2.s^2] + b1.s] + b0
 G(s) = ------ = -------------------------
         U(s)      [[a2.s^2] + a1.s] + a0

Please see development on :
    https://cours.hefr.ch/meca/asservissement_systemes_1/Cours/CoursASS12_oneSide.pdf
        chapter 12.3

@author: nicolas.rouve

"""

class LTI :
    def __init__ (self):
        self.last_time = 0
        self.h = 0 # means first exec (h = period )
        # print ('LTI initialised.')
  
    def measurePeriod (self,t):
        # compute the time elapsed since last iter in this version which is not "real-time" like it was in first versions,
        # elapsed time "h" is calculated with variable "t"
        self.this_time = t
        if self.last_time > 0 :
            self.h = (self.this_time - self.last_time) # compute time difference

        # if self.h==0: self.h=1e-9  # avoid further division by zero...

        self.last_time = self.this_time # remember time for the next loop
        # print('>> LTIsystem.LTI::measurePeriod: t=', self.this_time, 'h=', self.h)

# TODO: improve coefficients assignation, when list not fully completed

class system():
    def __init__(self, num , den):
       # ADD print TF
        if len(num)>2 or len(den)>2:
            self.sys = sysSecondOrder(num, den)
        else:
            self.sys = sysFirstOrder(num, den)

    def compute(self,uk, t): return self.sys.compute(uk, t)
            
class sysFirstOrder (LTI):
    def __init__(self, num = [0, 1], den = [0, 1]):
        LTI.__init__(self)
        #system parameters
        self.b1, self.b0 = num[0], num[1]
        self.a1, self.a0 = den[0], den[1]
        #initial conditions
        self.uk_1 = 0
        self.yk = self.yk_1 = 0

    def compute(self, uk, t):
        self.measurePeriod (t) # call function from parent class to get exec time

        #compute new output y, in this section uk_1 means u from last cycle
        denom = self.a0*self.h + 2*self.a1
        A1    = (self.a0*self.h - 2*self.a1) / denom      
        B0    = (self.b0*self.h + 2*self.b1) / denom
        B1    = (self.b0*self.h - 2*self.b1) / denom
        self.yk = B0*uk + B1*self.uk_1 - A1*self.yk_1
        
        self.uk_1 = uk    # keep u[k] to be last u (u[k_1]) on next cycle
        self.yk_1 = self.yk
        
        return self.yk
    
class sysSecondOrder (LTI):
    def __init__(self, num = [0, 0, 1], den = [0, 0, 1]):
        LTI.__init__(self)
        #system parameters
        self.b2, self.b1, self.b0 = num[0], num[1], num[2]
        self.a2, self.a1, self.a0 = den[0], den[1], den[2]
        #initial conditions
        self.uk_1 = self.uk_2 = 0
        self.yk = self.yk_1 = self.yk_2 = 0
        # xprint ("b:", self.b2, self.b1, self.b0, "a:", self.a2, self.a1, self.a0)

    def compute(self, uk, t):
        self.measurePeriod (t) # call function from parent class to get exec time

        #compute new output y, in this section uk_1 means u from last cycle
        denom = self.a0*self.h**2 + 2*self.a1*self.h + 4*self.a2          #  a0 h^2 + 2a1 h + 4a2
        
        B0 = (  self.b0*self.h**2 + 2*self.b1*self.h + 4*self.b2) / denom #  b0 h^2 + 2b1 h + 4b2
        A1 = (2*self.a0*self.h**2                    - 8*self.a2) / denom # 2a0 h^2 - 8a2
        B1 = (2*self.b0*self.h**2                    - 8*self.b2) / denom # 2b0 h^2 - 8b2
        A2 = (  self.a0*self.h**2 - 2*self.a1*self.h + 4*self.a2) / denom #  a0 h^2 - 2a1 h + 4a2
        B2 = (  self.b0*self.h**2 - 2*self.b1*self.h + 4*self.b2) / denom #  b0 h^2 - 2b1 h + 4b2
        self.yk = B0*uk + B1*self.uk_1 + B2*self.uk_2 - A1*self.yk_1 - A2*self.yk_2
        # print ('h={:.4f}\t A1={:.2f}\t A2={:.2f}\t B0={:.2f}\t B1={:.2f}\t B2={:.2f}\t '.format(self.h, A1, A2, B0, B1, B2), end='')
 
        # keep u[k] to be last u (u[k_1]) on next cycle
        self.uk_2, self.uk_1 = self.uk_1, uk
        self.yk_2, self.yk_1 = self.yk_1, self.yk
        
        return self.yk
    