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

i_V=initialize(0.72,0.007)
V=trajectory(i_V[0],i_V[1],i_V[2],i_V[3])
x_V=V[0]
y_V=V[1]

i_E=initialize(1.00,0.017)
E=trajectory(i_E[0],i_E[1],i_E[2],i_E[3])
x_E=E[0]
y_E=E[1]

i_Ma=initialize(1.52,0.093)
Ma=trajectory(i_Ma[0],i_Ma[1],i_Ma[2],i_Ma[3])
x_Ma=Ma[0]
y_Ma=Ma[1]

i_J=initialize(5.20,0.048)
J=trajectory(i_J[0],i_J[1],i_J[2],i_J[3])
x_J=J[0]
y_J=J[1]

i_S=initialize(9.54,0.056)
S=trajectory(i_S[0],i_S[1],i_S[2],i_S[3])
x_S=S[0]
y_S=S[1]

i_U=initialize(19.19,0.046)
U=trajectory(i_U[0],i_U[1],i_U[2],i_U[3])
x_U=U[0]
y_U=U[1]

i_N=initialize(30.06,0.010)
N=trajectory(i_N[0],i_N[1],i_N[2],i_N[3])
x_N=N[0]
y_N=N[1]

i_P=initialize(39.53,0.248)
P=trajectory(i_P[0],i_P[1],i_P[2],i_P[3])
x_P=P[0]
y_P=P[1]


#plot
figure(figsize=(10,10))
plot(x_M,y_M,color='red')
plot(x_V,y_V,color='orange')
plot(x_E,y_E,color='yellow')
plot(x_Ma,y_Ma,color='green')
plot(x_J,y_J,color='grey')
plot(x_S,y_S,color='blue')
plot(x_U,y_U,color='purple')
plot(x_N,y_N,color='pink')
plot(x_P,y_P,color='black')
legend(('Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'),'upper right')
title('Orbits of planets in solar system',fontsize=15)
xlabel('x/AU')
xlim(-30,50)
ylabel('y/AU')
ylim(-40,40)
show()


