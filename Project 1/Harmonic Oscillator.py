# Euler's method in two ways: with numpy and without

import numpy as np

# define the initial conditions here
t0 = 0
x0 = 1
h = .01
N = 100
def v(x,t):
    return -3*x

# do the euler's without numpy
def euler_python(t0,x0, v, h, N):
    solution_python = [[t0],[x0]]
    for i in range(1,N+1):
        prevT = solution_python[0][i-1]
        prevX = solution_python[1][i-1]
        solution_python[0].append(round(prevT+h,5))
        solution_python[1].append(round(prevX+h*v(prevX,prevT),5))
    return solution_python

# do the euler's with numpy
def euler_numpy(t0,x0, v, h, N):
    times = np.arange(t0,t0+h*N+h, h)
    position = np.zeros(len(times))
    position[0] = x0
    for i in range(1,len(times)):
        position[i] = position[i-1] + v(position[i-1],times[i-1])*h
    solution_numpy = np.array([times,position])
    return solution_numpy

#print numerical solution
solution = euler_numpy(t0,x0,v,h,N)
print(solution)

#import matplotlib to plot numerical and exact solution
import matplotlib.pyplot as plt

#plot numerical solution
plt.plot(solution[0],solution[1],color='r')
#plot exact solution for v = -3x
x = np.linspace(t0,N*h,100)
y = np.exp(-3*x)
plt.plot(x,y,color='g')

plt.show()