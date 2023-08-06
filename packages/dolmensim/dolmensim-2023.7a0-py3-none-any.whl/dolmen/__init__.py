# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:19:55 2023

@author: vujic
"""

from dolmen import (
   mechanics,
   control,
   electrics,
   utils,
   aeronautics
   )

from .mechanics import (
   kinematics as kin,       # getVector (DCM)
   dynamics as dyn,         # Gravity, Newton
   rotational as rot,       # Reducer, Wheel
   inertia as ir,           # inertia calculations
   fluidsMechanics as fm    # Air, Adim(Reynolds, Mach), Archimedes
   )

from .control import(
    pid as ctl#             # PIC rectifier
    )

from .electrics import(
    motors as mot           # TorqueMotor, Motor
    )

from .utils import (
   frameworkV9 as fwk,      # System, Dimension, Quantity, RK4()
   misc as misc,            # Totalizer, cart2pol(), pol2cart(), cart2spher(), spher2cart(), vectProject()
   dataTable as tbl,        # Profile, dataFile, aeroCoef
   volumes as vol,          # volumes...
   rho as rho,              # get material or alloys densities
   cog as cg                # center of Gravity
   )

from .aeronautics import(
    gear as gear,           # Tire
    aerodynamics as aero    # Wing, Foil, Propeller, Fuselage, Aerocoef
    )