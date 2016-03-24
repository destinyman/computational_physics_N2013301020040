#!/usr/bin/env python
# encoding: utf-8

from pylab import *
import pickle

N_number = []
t = []
a = 0
b = 0
dt = 0
n = 0

def initialize(N_number, t, _a, _b, _dt, _n):
    global a, b, dt, n
    print "initial number of population -> ",
    N_number.append(float(raw_input()))
    print "constant coefficient A -> ",
    a = float(raw_input())
    print "constant coefficient B -> ",
    b = float(raw_input())
    print "time step -> ",
    dt = float(raw_input())
    print "total time -> ",
    time = float(raw_input())
    t.append(0)
    n = int(time / dt)
    return 0

def calculate(N_number, t, a, b, dt, n):
    print N_number
    print t
    print a
    print b
    print dt
    print n
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

initialize(N_number, t, a, b, dt, n)
calculate(N_number, t, a, b, dt, n)
store(N_number, t, n)

plot(t, N_number, '--*')
# scatter(t, N_number)
show()
savefig("test_.jpg")

read()

