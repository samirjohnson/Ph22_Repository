from Vector import *
import math
import matplotlib.pyplot as plt
import numpy as np

def RK4(vec, t, h, func):
    k1 = h * func(vec, t)
    k2 = h * func(vec + k1/2, t + h/2)
    k3 = h * func(vec + k2/2, t + h/2)
    k4 = h * func(vec + k3, t + h)
    return vec + 1/6 * (k1 + k2 + k3 + k4)

def evaluateODE(vecINIT, h, func, N):
    tList = np.linspace(0, N, int(N / h + 1))
    vecList = [vecINIT]
    for i in range(0,int(N/h)):
        vecList.append(RK4(vecList[i], tList[i], h, func))
    return vecList

def func(vec, t):
    return Vector([vec[1], - vec[0] / math.pow(math.pow(vec[0],2) + math.pow(vec[2],2), 3/2),
                  vec[3], - vec[2] /  math.pow(math.pow(vec[0],2) + math.pow(vec[2],2), 3/2)])

vecINIT = Vector([1,0,0,10]); R = 1; h = 0.0001; N = 10;

xList = []; yList = [];
vecList = evaluateODE(vecINIT, h, func, N)
for v in vecList:
    xList.append(v[0]); yList.append(v[2]);

plt.plot(xList, yList)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
