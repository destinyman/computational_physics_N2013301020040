#!/usr/bin/env python
# encoding: utf-8

from pylab import *
import pickle

#define variables relevent
v=[]
t=[0]
g=9.8
n=0
dt=0

#set initial values
def initialize(v, t, _dt, _n):
    global dt, n 
    v.append(float(raw_input("initial velocity -> ")))
    dt = float(raw_input("time step -> "))
    time = float(raw_input("total time -> "))
    n = int(time / dt)
    return 0

def calculate(v, t, dt, n):
    for i in range(1, n):
        v.append(v[i-1]+g*dt)
        t.append(t[i-1] + dt)
    return 0

def store(v, t, n):
    mfile = open("notes.txt", "a")
    for i in range(n):
        print >> mfile, t[i], v[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(v, pickle_file)
    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    v = pickle.load(pickle_file)
    print t
    print v



initialize(v, t, dt, n)
calculate(v,t, dt, n)
store(v, t, n)

# create a picture of 8 * 6 point, and set the resolution as 80
figure(figsize=(8,6), dpi=80)

# plot the curve
plot(t, v,label='simulation of freely falling object', color="blue", linewidth=2.5, linestyle = "--")
legend(loc='upper center')

# set the limit of the x-axial and y-axial
xlim(0,max(t))
ylim(min(v),max(v))


ylabel('velocity v')
xlabel('time t')


#display and show the picture
show()
savefig("test_1.jpg")
read()





