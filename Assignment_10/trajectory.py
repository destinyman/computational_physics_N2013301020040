from pylab import *

x=[]
y=[]
z=[]
t=[]
a=10.
b=8./3.
r=25
dt=0.0001
x1=[]
y1=[]
z1=[]

def initialize(_x,_y,_z,_a,_b,_r,_dt,_t):
    global a,b,r,dt,x,y,z,t
    x=[]
    y=[]
    z=[]
    t=[]
    a=10.
    b=8./3.
    r=25
    dt=0.0001
    x.append(1)
    y.append(0)
    z.append(0)
    t.append(0)

def calculate(x,y,z,t):
    while (t[-1]<100):
        x.append(x[-1]+dt*(a*(y[-1]-x[-1])))
        y.append((-x[-1]*z[-1]+r*x[-1]-y[-1])*dt+y[-1])
        z.append(z[-1]+dt*(x[-1]*y[-1]-b*z[-1]))
        t.append(t[-1]+dt)
        
        
initialize(x,y,z,a,b,r,dt,t)
calculate(x,y,z,t)

plot(x,z,label='lorent model: z versus time')
legend(loc='upper center')

xlabel('t')
ylabel('z')

show()

