#!/usr/bin/env python
# encoding: utf-8

from pylab import *
import pickle

#define variables relevent
N = []
t = [0]
a = 0.
b = 0.
dt = 0.
n = 0

#set initial values
def initialize(N, t, _a, _b, _dt, _n):
    global a, b, dt, n
    N.append(float(raw_input("initial number of population -> ")))
    a = float(raw_input("constant coefficient A -> "))
    b = float(raw_input("constant coefficient B -> "))
    dt = float(raw_input("time step -> "))
    time = float(raw_input("total time -> "))
    n = int(time / dt)
    return 0

def calculate(N, t, a, b, dt, n):
    for i in range(1, n):
        N.append(N[i - 1] + (a*N[i - 1] - b*N[i - 1]**2) * dt)
        t.append(t[i - 1] + dt)
    return 0

def store(N, t, n):
    mfile = open("notes.txt", "a")
    for i in range(n):
        print >> mfile, t[i], N[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(N, pickle_file)
    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    N = pickle.load(pickle_file)
    print t
    print N



initialize(N, t, a, b, dt, n)
calculate(N, t, a, b, dt, n)
store(N, t, n)

# create a picture of 8 * 6 point, and set the resolution as 80
figure(figsize=(8,6), dpi=80)

# plot the curve
plot(t, N,label='simulation of population growth model', color="blue", linewidth=1.0, linestyle = "--")
legend(loc='upper center')

# set the limit of the x-axial and y-axial
xlim(0,max(t))
ylim(min(N)/1.01,max(N)*1.01)

if a >= b*N[0]:
    plot([0,max(t)],[max(N),max(N)],label='the terminal population', color='red',    linewidth=2.5, linestyle="--")
else:
    plot([0,max(t)],[min(N),min(N)],label='the terminal population', color='red',    linewidth=2.5, linestyle="--")


ylabel('population N')
xlabel('time t')


#display and show the picture
show()
savefig("test_1.jpg")
read()





