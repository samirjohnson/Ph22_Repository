from Vector import *
from RK4 import evaluateODE
import math
import matplotlib.pyplot as plt
import numpy as np

def func(vec, t):
    return Vector([vec[1], - vec[0] / math.pow(math.pow(vec[0],2) + math.pow(vec[2],2), 3/2),
                  vec[3], - vec[2] /  math.pow(math.pow(vec[0],2) + math.pow(vec[2],2), 3/2)])

vecINIT = Vector([1,0,0,1]); R = 1; h = 0.0001; N = 10;

xList = []; yList = [];
vecList = evaluateODE(vecINIT, h, func, N)
for v in vecList:
    xList.append(v[0]); yList.append(v[2]);

plt.plot(xList, yList)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
