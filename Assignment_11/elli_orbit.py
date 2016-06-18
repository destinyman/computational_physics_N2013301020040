"""
  simulation of solar system
"""

from math import * 
import numpy as np 
from pylab import *

def trajectory(x0,y0,vx0,vy0):
    x=[]
    y=[]
    vx=[]
    vy=[]
    r=[]
    dt=0.002
    t=300
#------------------------------------------------
    x.append(x0)
    y.append(y0)
    vx.append(vx0)
    vy.append(vy0)
    r.append(x0**2+y0**2)
#---------------------------------------------------

    for i in range(int(t/dt)):
        vx.append(vx[i]-4*pi**2*x[i]*r[i]**(-3)*dt)
        x.append(x[i]+vx[i+1]*dt)
        vy.append(vy[i]-4*pi**2*y[i]*r[i]**(-3)*dt)
        y.append(y[i]+vy[i+1]*dt)
        r.append(sqrt(x[i+1]**2+y[i+1]**2))
    return [x,y,vx,vy,r]

def initialize(a,e):
    x0=a*(1+e)
    y0=0
    vx0=0
    vy0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,y0,vx0,vy0]

#The orbits of 9 planets
i_M=initialize(0.39,0.206)
M=trajectory(i_M[0],i_M[1],i_M[2],i_M[3])
x_M=M[0]
y_M=M[1]


i_E=initialize(1.00,0.017)
E=trajectory(i_E[0],i_E[1],i_E[2],i_E[3])
x_E=E[0]
y_E=E[1]



#plot
figure(figsize=(10,10))
plot(x_E,y_E)
title('Simulation of elliptical orbit',fontsize=15)
xlabel('x/AU')
ylabel('y/AU')
show()


