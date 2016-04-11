#!/usr/bin/env python
# encoding: utf-8

from pylab import *
import math
import pickle

#declare necessary variables 
g=9.8
x=[0]
y=[0]
v=[]
a=0.
vx=[]
vy=[]
dt=0.
c=[]
r=[]
fx=[]
fy=[]
A=0.00002256
n=2.5
vx1=0.
vy1=[]
x1=[0]
y1=[0]
i=1
j=1

def initialize(_v, _a, _vx, _vy, _dt, _vx1, _vy1, _i, _j) :
    global v, a, vx, vy, dt, vx1, vy1, i, j
    v.append(float(raw_input("initial velocity of the shell ->")))
    a = float(raw_input("firing angle of the shell ->"))
    vx.append(v[0]*math.cos(math.radians(a)))
    vy.append(v[0]*math.sin(math.radians(a)))
    dt=float(2*vy[0]/g/100)
    vx1=vx[0]
    vy1.append(vy[0])
    i=1
    j=1
    return 0

# calculate trajectory of shell with friction
def calculate1(v,c,r,vx,vy,fx,fy,x,y,i):
    while int(y[i-1])>=0 and (1.0-A*y[i-1])>0:
        v.append(vx[i-1]**2+vy[i-1]**2)
        c.append((1.-A*y[i-1])**n)
        r.append(0.00004*v[i-1])
        fx.append(c[i-1]*r[i-1]*vx[i-1])
        fy.append(c[i-1]*r[i-1]*vy[i-1])
        vx.append(vx[i-1]-fx[i-1]*dt)
        vy.append(vy[i-1]-g*dt-fy[i-1]*dt)
        x.append(x[i-1]+vx[i-1]*dt)
        y.append(y[i-1]+vy[i-1]*dt)
        i=i+1
    return 0

# calculate the trajectory of shell without friction
def calculate(x1,vy1,y1,j):
    while (y1[j-1]>=0): 
        x1.append(x1[j-1]+vx1*dt)
        vy1.append(vy1[j-1]-g*dt)
        y1.append(y1[j-1]+vy1[j-1]*dt)
        j=j+1
    return 0

initialize(v, a, vx, vy, dt, vx1, vy1, i, j)
calculate1(v,c,r,vx,vy,fx,fy,x,y,i)
calculate(x1,vy1,y1,j)

# create a picture of 8 * 6 point, and set the resolution as 80
figure(figsize=(8,6), dpi=80)

# plot the curve
plot(x, y,label='with friction', color="blue", linewidth=2.5, linestyle = "--")
plot(x1, y1,label='without frictoin', color="red", linewidth=2.0, linestyle = "--")
legend(loc='upper center')

# set the limit of the x-axial and y-axial
xlim(0,max(x1)*1.05)
ylim(0,max(y1)*1.2)

# marke the axis
ylabel('vertical height y/m')
xlabel('herizonal distance x/m')


#display and show the picture
show()
savefig("test_1.jpg")

