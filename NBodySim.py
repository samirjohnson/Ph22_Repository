from Vector import *
from SymplecticIntegrator import *
import math
import numpy as np
import matplotlib.pyplot as plt
from random import random

M = 1; G = 1; R = 1; a = 0.1; N = 40;
tfinal = 2*math.pi*math.sqrt(R**3/(G*M)); timestep = tfinal/1000;

def func(vec, t, h):
    acc = lambda x1, x2: -G * M * (x1 - x2) / (Vector.magnitude(x1 - x2)**(3) + Vector.magnitude(x1 - x2)*a**2)
    xvec = Vector([None]*int(len(vec)/2)); vvec = Vector([None]*len(xvec));
    for i in range(len(xvec)):
        f = Vector([0,0])
        for j in range(len(vvec)):
            if i!=j:
                q = acc(vec[2*i], vec[2*j])
                f[0] += q[0]; f[1] += q[1];
        vvec[i] = f; xvec[i] = vec[2*i+1] + h*f
    retvec = Vector([None]*len(vec)); retvec[::2] = xvec; retvec[1::2] = vvec;
    return retvec

vecINIT = Vector([0] * 2 * N)
for i in range(2*N):
    theta1 = 2 * math.pi * random(); theta2 = 2 * math.pi * random();
    if i % 2 == 0:
        vecINIT[i] = R*Vector([math.cos(theta1), math.sin(theta1)])
    else:
        vecINIT[i] = 0.1*Vector([math.cos(theta2),math.sin(theta2)])

vecList = evaluateODE(vecINIT, timestep, func, tfinal)

xList = []
yList = []
for v in vecList:
    for i in v:
        if v.index(i)%2==0:
            xList.append(i[0]); yList.append(i[1]);

for i in range(N):
    plt.plot(xList[i::N], yList[i::N])
plt.xlabel('X'); plt.ylabel('Y');
plt.show()
