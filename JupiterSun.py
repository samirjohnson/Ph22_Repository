import math
import matplotlib.pyplot as plt
import numpy as np
from Vector import *
from RK4 import RK4, evaluateODE

M1 = 1.899 * 10**29; M2 = 1.989 * 10**30; G = 6.6742 * 10**(-11);
R = 778.3 * 10**9; T = 3.743 * 10**8;
r1 = Vector([M2 * R / (M1 + M2), 0, 0]); r2 = Vector([-M1 * R / (M1 + M2), 0, 0]);
O = math.sqrt(G * (M1 + M2) / (R**3))
alpha = math.pi / 8
rInit = R * Vector([(M2 - M1)/(M1 + M2) * math.cos(alpha), math.sin(alpha), 0])

def func(vec, t):
    r = Vector([vec[0], vec[2], 0])
    acc = -G*M1/Vector.magnitude(r-r1)**3 * (r-r1) - G*M2/Vector.magnitude(r-r2)**3 * (r-r2) + 2*O*Vector([vec[3], -vec[1], 0]) + O**2 * r
    return Vector([vec[1], acc[0], vec[3], acc[1]])

N = 2*T; h = T / 1000;
xList = []; yList = [];
vecInit = Vector([rInit[0], 0, rInit[1], 0])
vecList = evaluateODE(vecInit, h, func, N)
for v in vecList:
    xList.append(v[0]); yList.append(v[2]);

plt.plot(xList, yList); plt.xlabel("X"); plt.ylabel("Y"); plt.show();
