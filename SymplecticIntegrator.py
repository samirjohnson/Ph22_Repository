from Vector import *
import math
import numpy as np

def SympInt(vec, t, h, func):
    return vec + h * func(vec, t, h)

def evaluateODE(vecINIT, h, func, N):
    tlist = np.linspace(0, N, int(N/h + 1))
    vecList = [0] * len(tlist); vecList[0] = vecINIT;
    for i in range(1,int(N/h)+1):
        vecList[i] = SympInt(vecList[i-1], tlist[i-1], h, func)
    return vecList
