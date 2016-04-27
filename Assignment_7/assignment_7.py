from pylab import *
import numpy as np

g=9.8
s0m=4.1E-4
x=[]
y=[]
vx=[]
vy=[]
omega=0.
t=[]
fx=[]
fy=[]
b2m=[]
v=[]
alpha=0.
dt=0.
i=1

def initialize(_x,_y,_v,_alpha,_vx,_vy,_omega,_t,_dt,_fx,_fy,_i,_b2m):
    global x,y,v,alpha,vx,vy,omega,t,dt,fx,fy,i,b2m
    x.append(0)
    y.append(0)
    omega=2000*2*3.14159/60
    v.append(float(raw_input("initial velocity of the baseball -> ")))
    alpha=float(raw_input("initial angle of the baseball -> "))
    vx.append(v[0]*np.cos(np.radians(alpha)))
    vy.append(v[0]*np.sin(np.radians(alpha)))
    dt=0.1
    i=1

def calculate(v,b2m,vx,vy,fx,fy,x,y,i):
    while y[i-1]>=0:
        v.append(vx[i-1]**2+vy[i-1]**2)
        b2m.append(0.0039+0.0058/(1+np.exp((v[i-1]-35)/5)))
        fx.append(b2m*v[i-1]*vx[i-1])
        fy.append(b2m*v[i-1]*vy[i-1]-s0m*vx[i-1]*omega)
        vx.append(vx[i-1]-fx[i-1]*dt)
        vy.append(vy[i-1]-g*dt-fy[i-1]*dt)
        x.append(x[i-1]+vx[i-1]*dt)
        y.append(y[i-1]+vy[i-1]*dt)
        i=i+1
    return 0

initialize(x,y,v,alpha,vx,vy,omega,t,dt,fx,fy,i,b2m)
calculate(v,b2m,fx,fy,vx,vy,x,y,i)

plot(x,y,label='trejectory of batted ball')
legend(loc='upper center')
ylabel('vertical height y/m')
xlabel('herizonal distance x/m')


