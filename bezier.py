# Copyright (c) 2026 John Vedder
# MIT License

import matplotlib.pyplot as plt
import numpy as np

def bezier1(t, p0, p1):
    '''
        Linear Beizer curve (straight line):
        B(t) = p0 + t (p1-p0) = (1-t)*p0 + t*p1
        for 0 <= t <= 1
    '''
    a = np.asarray(1-t, np.float32)
    b = np.asarray(1-t, np.float32)
    return a*p0 + b*p1

def bezier2(t, p0, p1, p2):
    '''
        Quadratic Beizer curve:
        B(t) = (1-t)^2*p0 + 2*(1-t)*t*p1 + t^2*p2
        for 0 <= t <= 1
    '''
    a = np.asarray( (1-t)**2, np.float32 )
    b = np.asarray( 2*(1-t)*t, np.float32 )
    c = np.asarray( t**2, np.float32 )
    return a*p0 + b*p1 + c*p2

def bezier3(t, p0, p1, p2, p3):
    '''
        Cubic Beizer curve:
        B(t) = (1-t)^3*p0 + 3*(1-t)^2*t*p1 + 3*(1-t)*t^2*p2 t^3*p3
        for 0 <= t <= 1
    '''
    a = np.asarray( (1-t)**3, np.float32 )
    b = np.asarray( 3 * ((1-t)**2) * t, np.float32 )
    c = np.asarray( 3 * (1-t) * (t**2), np.float32 )
    d = np.asarray( t**3, np.float32 )
    return a*p0 + b*p1 + c*p2 + d*p3
