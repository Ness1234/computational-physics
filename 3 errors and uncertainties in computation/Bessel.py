# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:13:51 2020

@author: nz
"""
from vpython import *
import numpy as np

Xmax = 40.
Xmin = 0.25
step = 0.1
order = 10 ; start = 50
graph1 = graph(width = 500, height = 500, title = 'Spherical Bessel L =1 (red), 10',
               xtitle = 'x', ytitle = 'j(x)', xmin = Xmin, xmax = Xmax,
               ymin = -0.2, ymax = 0.5)
funct1 = gcurve(color = color.red)
funct2 = gcurve(color = color.green)

def down(x,n,m):    #method down, recurs downward
    j = np.zeros((start+2),float)
    j[m+1]=j[m]=1.      #start with anything
    for k in range(m,0,-1):
        j[k-1]=((2.*k+1.)/x)*j[k]-j[k+1]
    scale = (np.sin(x)/x)/j[0]     #scale solution to known j[0]
    return j[n]*scale

for x in np.arange(Xmin, Xmax, step):
    funct1.plot(pos = vector(x, down(x, order, start)))

for x in np.arange(Xmin, Xmax, step):
    funct2.plot(pos = vector(x, down(x,1,start)))