from Vector import *
from RK4 import evaluateODE
import math
import matplotlib.pyplot as plt
import numpy as np

M1 = 1; M2 = 1; M3 = 1; G = 1;

def func(vec, t):
    acc = lambda ri, rj, rk, m1, m2: G*(m1*(rj-ri)/(Vector.magnitude(ri-rj))**(3) + m2*(rk-ri)/(Vector.magnitude(ri-rk))**(3))
    dv1 = acc(Vector([vec[0],vec[2]]), Vector([vec[4], vec[6]]), Vector([vec[8], vec[10]]), M2, M3)
    dv2 = acc(Vector([vec[4],vec[6]]), Vector([vec[0], vec[2]]), Vector([vec[8], vec[10]]), M1, M3)
    dv3 = acc(Vector([vec[8],vec[10]]), Vector([vec[4], vec[6]]), Vector([vec[0], vec[2]]), M2, M1)
    return Vector([vec[1], dv1[0], vec[3], dv1[1], vec[5], dv2[0], vec[7], dv2[1], vec[9], dv3[0], vec[11], dv3[1]])

#X = 0.97000436; Y = -0.24308753; VX = -0.93240737; VY = -0.86473146;
#vecInit = Vector([X,-VX/2,Y,-VY/2,-X,-VX/2,-Y,-VY/2,0,VX,0,VY])
vecInit = Vector([1,1,0,0,0,0,1,1,-1,-1,0,0])
x1 = []; y1 = []; x2 = []; y2 = []; x3 = []; y3 = []; N = 10; h = N/1000;
vecList = evaluateODE(vecInit, h, func, N)
for v in vecList:
    x1.append(v[0]); y1.append(v[2]);
    x2.append(v[4]); y2.append(v[6]);
    x3.append(v[8]); y3.append(v[10]);

plt.plot(x1, y1, x2, y2, x3, y3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
