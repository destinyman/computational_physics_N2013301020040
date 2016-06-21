"""
    This is the original code for the final exam of computational physics
    Auther: wu weipeng          last modify: 2016.6.19
"""
import matplotlib.pyplot as plt
import math
#from mpl_toolkits.mplot3d import Axes3D
#from pylab import *

g = 9.8
b2m = 4e-5
a = 2.17e-5
b = 2.5
omega = 1.75e-3

# the state class of flight
class flight_state:
    def __init__(self, _x = 0, _y = 0, _z =0, _vx = 0, _vy = 0, _vz =0, _t = 0):
        self.x = _x
        self.y = _y
        self.z = _z
        self.vz = _vz
        self.vx = _vx
        self.vy = _vy
        self.t = _t
# cannon class that analog cannon's state
class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
#        print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy 
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz - g * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_z, next_vx, next_vy, next_vz, current_state.t + self.dt)

    def shoot(self):
        while not(self.cannon_flight_state[-1].z < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
#            print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

        r = - self.cannon_flight_state[-2].z / self.cannon_flight_state[-1].z
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = (self.cannon_flight_state[-2].y + r * self.cannon_flight_state[-1].y) / (r + 1)
        self.cannon_flight_state[-1].z = 0

    def show_trajectory(self):
        x = []
        y = []
        z = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
            z.append(fs.z)


#plot(x,y)
        plt.subplot(131)
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.legend(loc='upper center')
        plt.plot(x,y,label='x versus y in the trace')

#plot(x,z)
        plt.subplot(132)
        plt.xlabel('x/m')
        plt.ylabel('z/m')
        plt.legend(loc='upper center')
        plt.plot(x,z,label='x versus z in the trace')
#plot(y,z)
        plt.subplot(133)
        plt.xlabel('y/m')
        plt.ylabel('z/m')
#        plt.title('trejectory')
        plt.legend(loc='upper center')
        plt.plot(y,z,label='y versus z in the trace')
        #show()

class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = math.sqrt(current_state.vx **2 + current_state.vy **2 + current_state.vz **2)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz - g * self.dt - b2m * v * current_state.vz * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - b2m * v * current_state.vy * self.dt
        #print next_x, next_y, next_z
        return flight_state(next_x, next_y, next_z, next_vx, next_vy, next_vz, current_state.t + self.dt)

class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m, a, b
        v = math.sqrt(current_state.vx **2 + current_state.vy **2 + current_state.vz **2)
        next_x = current_state.x + current_state.vx * self.dt     
        next_z = current_state.z + current_state.vz * self.dt      
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - b2m * v * current_state.vy * self.dt * ((1 - a * current_state.z)**b)
        next_vx = current_state.vx - b2m * v * current_state.vx * (1. - a * current_state.z) * self.dt 
        next_vz = current_state.vz - g * self.dt - b2m * v * current_state.vz * self.dt * ((1-a*current_state[-1].z)**b)
        
        
        #print next_x, next_y, next_z
        return flight_state(next_x, next_y, next_z, next_vx, next_vy, next_vz, current_state.t + self.dt)

class Coliorio_connon(cannon):
    def next_state(self, current_state):
        global g, b2m, a, b, omega
        v = math.sqrt(current_state.vx **2 + current_state.vy **2 + current_state.vz **2)
        next_x = current_state.x + current_state.vx * self.dt    
        next_z = current_state.z + current_state.vz * self.dt    
        next_y = current_state.y + current_state.vy * self.dt

        next_vx = current_state.vx - b2m * v * current_state.vx * (1. - a * current_state[-1].z) * self.dt + omega * current_state.vz * self.dt
        next_vy = current_state.vy - b2m * v * current_state.vy * self.dt * ((1-a * self.cannon_flight_state[-1].z)**b)
        next_vz = current_state.vz - g * self.dt - b2m * v * current_state.vz * self.dt * ((1-a*current_state[-1].z)**b) - omegaa * current_state.vx * self.dt
        return flight_state(next_x, next_y, next_z, next_vx, next_vy, next_vz, current_state.t + self.dt)

a = cannon(flight_state(0, 0, 0, 50, 50, 50, 0), _dt = 0.1)
a.shoot()
b = drag_cannon(flight_state(0, 0, 0, 50, 50, 50, 0), _dt = 0.1)
b.shoot()
c= adiabatic_drag_cannon(flight_state(0, 0, 0, 50, 50, 50, 0), _dt = 0.1)
c.shoot()
d.Coliorio_connon(flight_state(0, 0, 0, 50, 50, 50, 0), _dt = 0.1)
d.shoot
a.show_trajectory()
b.show_trajectory()
c.show_trajectory()
d.show_trajectory()
plt.show()
#show()
