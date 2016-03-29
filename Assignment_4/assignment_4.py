#!/usr/bin/env python
# encoding: utf-8

from pylab import *
import pickle

#define variables relevent
N_number = []
t = []
a = 0.
b = 0.
dt = 0.
n = 0

#
def initialize(N_number, t, _a, _b, _dt, _n):
    global a, b, dt, n
    N_number.append(float(raw_input("initial number of population:")))
    a = float(raw_input("constant coefficient A -> "))
    b = float(raw_input("constant coefficient B -> "))
    dt = float(raw_input("time step -> "))
    time = float(raw_input("total time -> "))
    t.append(0)
    n = int(time / dt)
    return 0

def calculate(N_number, t, a, b, dt, n):
    for i in range(1, n):
        N_number.append(N_number[i - 1] + (a*N_number[i - 1] - b*N_number[i - 1]**2) * dt)
        t.append(t[i - 1] + dt)
    return 0

def store(N_number, t, n):
    mfile = open("notes.txt", "a")
    for i in range(n):
        print >> mfile, t[i], N_number[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(N_number, pickle_file)

    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    N_number = pickle.load(pickle_file)
    print t
    print N_number

#limit maximum N and t to shorten the photo
xmin,xmax=min(t),max(t)
ymin,ymax=min(N_number),max(N_number)


initialize(N_number, t, a, b, dt, n)
calculate(N_number, t, a, b, dt, n)
store(N_number, t, n)

plot(t, N_number, '--*')
# scatter(t, N_number)
xlabel=('time t')
ylabel=('population N')
show()
savefig("test_.jpg")

read()

