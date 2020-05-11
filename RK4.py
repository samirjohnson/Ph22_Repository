from Vector import *
import math
import numpy as np

def RK4(vec, t, h, func):
    k1 = h * func(vec, t)
    k2 = h * func(vec + k1/2, t + h/2)
    k3 = h * func(vec + k2/2, t + h/2)
    k4 = h * func(vec + k3, t + h)
    return vec + 1/6 * (k1 + k2 + k3 + k4)

def evaluateODE(vecINIT, h, func, N):
    tList = np.linspace(0, N, int(N / h + 1))
    vecList = np.zeros(len(tList)); vecList[0] = vecINIT;
    for i in range(1,int(N/h)+1):
        vecList[i] = RK4(vecList[i-1], tList[i-1], h, func)
    return vecList
