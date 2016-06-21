import math 
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

g = 9.8
b2m = 4e-5
a1 = 2.17e-5
b1 = 2.5
#omega = 1.75e-3
dt = 0.001
theta = 20 

#b2m = 0
#a1 =0
#b1 = 0
omega = 0



def calculate1():
    global g,b2m,a1,b1,omega,dt, theta
    x=[0.]
    y=[0.]
    z=[0.]
    vx=[0.]
    vy=[0.]
    vz=[0.]
    v=[0.]
    r=[0,0]
#-----------------------------------------------
    x.append(0.)
    y.append(0.)
    z.append(0.)
    v.append(700.)
    vx.append(0.)
    ra = theta * math.pi / 180 
    vy.append(700.*cos(ra))
    vz.append(700.*sin(ra))
    while (r[-1]>=r[-2]):
        
        while not(z[-1]<0):
            v.append(math.sqrt(vx[-1]**2+vy[-1]**2+vz[-1]**2))
            x.append(x[-1]+vx[-1]*dt)
            y.append(y[-1]+vy[-1]*dt)
            z.append(z[-1]+vz[-1]*dt)

            vx.append(vx[-1] - b2m * v[-1] * vx[-1] * (1.0- a1 * z[-1]) ** b1 * dt + omega * vz[-1] * dt)
            vy.append(vy[-1] - b2m * v[-1] * vy[-1] * (1.0- a1 * z[-1]) ** b1 * dt )
            vz.append(vz[-1]-g*dt - b2m * v[-1] * vz[-1] * (1.0- a1 * z[-1]) ** b1 * dt - omega * vx[-1] * dt)
           

#        r.append((y[-2]-(z[-2]/z[-1])*y[-1]/(1-z[-2]/z[-1]))**2+(x[-2]-(z[-2]/z[-1])*x[-1]/(1-z[-2]/z[-1]))**2)
        r.append(math.sqrt(x[-1]**2 + y[-1]**2 + z[-1]**2))
        x=[0]
        y=[0]
        z=[0]
        vx=[0]
        vy=[0]
        vz=[0]
        v=[0]
        theta = theta + 1
        ra = theta * math.pi / 180
        x.append(0)
        y.append(0)
        z.append(0)
        v.append(700)
        vx.append(0)
        vy.append(700*cos(ra))
        vz.append(700*sin(ra))
    print theta,r[-1]
    return 0
calculate1()
show()

    
    
    
