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

def initialize(_v, _a, _vx, _vy, _dt, _c, _r, _fx, _fy) :
    global v, a, vx, vy, dt, c, r, fx, fy
    v.append(float(raw_input("initial velocity of the shell ->")))
    a = float(raw_input("firing angle of the shell ->"))
    vx.append(v[0] * math.cos(math.radians(a)))
    vy.append(v[0] * math.sin(math.radians(a)))
    dt = float(vx[0]*(2*vy[0]/g)/10000)
    c.append(float((1-A*y[0])**n))
    r.append(float(0.00004*v[0]))
    fx.append(c[0]*r[0]*vx[0])
    fy.append(c[0]*r[0]*vy[0])
    return 0

def calculate(c, r, vx, vy, fx, fy, v, x, y):
    while y>0 :
        for i in range(1,1000):
            c.append(pow((1-A*y[i-1]),n))
            r.append(0.00004*v[i-1])
            vx.append(vx[i-1]-fx[i-1]*dt)
            vy.append(vy[i-1]-g*dt-fy[i-1]*dt)
            fx.append(c[i-1]*r[i-1]*vx[i-1])
            fy.append(c[i-1]*r[i-1]*vy[i-1])
            v.append(vx[i-1]**2+vy[i-1]**2)
            x.append(x[i-1]+vx[i-1]*dt)
            y.append(y[i-1]+vy[i-1]*dt)
        return 0

#store data for trace with frictions
def store(y, x):
    mfile = open("notes.txt", "a")
    for i in range(1,1000):
        print >> mfile, x[i], y[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(x, pickle_file)
    pickle.dump(y, pickle_file)
    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    x = pickle.load(pickle_file)
    y = pickle.load(pickle_file)
    print x
    print y


initialize(v, a, vx, vy, dt, c, r, fx, fy)
calculate(c, r, vx, vy, fx, fy, v, x, y)
store(y, x)


# create a picture of 8 * 6 point, and set the resolution as 80
figure(figsize=(8,6), dpi=80)

# plot the curve
plot(x, y,label='simulation of firing a shell', color="blue", linewidth=2.0, linestyle = "--")
legend(loc='upper center')

# set the limit of the x-axial and y-axial
xlim(0,max(x)*1.05)
ylim(0,max(y)*1.2)


ylabel('vertical height y/m')
xlabel('herizonal distance x/m')


#display and show the picture
show()
savefig("test_1.jpg")
read()

