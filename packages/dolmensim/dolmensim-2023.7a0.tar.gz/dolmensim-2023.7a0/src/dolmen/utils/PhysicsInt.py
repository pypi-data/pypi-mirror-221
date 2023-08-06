# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:20:54 2023

@author: vujic
"""

def run_kut4(x, F, t, h):
    """
    Created on Thu Mar 10 09:50:23 2022
    
    @author: Vincent Bourquin
    """
    '''
    Méthode de Runge-Kutta du 4ème ordre pour résoudre le
    problème aux valeurs initiales {x}' = {F(t,{x})}, où
    {x} = {x[0],x[1],...x[n-1]}.
    t,x = conditions initiales
    tStop = valeur finale de t (marquant la fin de l'intégration)
    h = incrément de t utilisé pour l'intégration'
    F = fonction à intégrer décrite par l'utilisateur et retournant
    le array F(t,x) = {x'[0],x'[1],...,x'[n-1]}.
    Cette méthode permet la résolution numérique des équations différentielles 
    en général et celles dérivant de l'équation de Newton en particulier'
    cf: https://femto-physique.fr/analyse-numerique/runge-kutta.php
    '''
    k1 = h*F(t,         x          )[0] # index to get 1st array : new values
    k2 = h*F(t + h/2.0, x + k1/2.0 )[0] # "
    k3 = h*F(t + h/2.0, x + k2/2.0 )[0] # "
    k4 = h*F(t + h,     x + k3     )[0] # "
    increase = (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    result = x + increase
    # print ('.', end='')
    # print ('t=',t,' x=', result)
    return result