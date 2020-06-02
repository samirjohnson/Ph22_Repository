from Vector import *
from SymplecticIntegrator import *
import math
import numpy as np
import matplotlib.pyplot as plt
from random import random

M = 1; G = 1; R = 1; a = 0.1; N = 100; tdyn = math.sqrt(R**3/(G*M*N));
tfinal = 6*math.pi*tdyn; timestep = 0.005; trelax = N / (10 * math.log(N)) * tdyn;

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

#initialize particles within ring of radius R
vecINIT = Vector([0] * 2 * N)
for i in range(2*N):
    theta1 = 2 * math.pi * random(); theta2 = 2 * math.pi * random();
    if i % 2 == 0:
        vecINIT[i] = random()*R*Vector([math.cos(theta1), math.sin(theta1)])
    else:
        vecINIT[i] = Vector.magnitude(vecINIT[i-1])/10*Vector([math.cos(theta2),math.sin(theta2)])

vecList = evaluateODE(vecINIT, timestep, func, tfinal)

radialPos = []; radialV = []; xList = []; yList = [];
for v in vecList:
    for i in v:
        if v.index(i)%2==0:
            radialPos.append(Vector.magnitude(i))
            xList.append(i[0]); yList.append(i[1]);
        else:
            radialV.append(Vector.magnitude(i))

tList = np.linspace(0,tfinal, int(len(radialPos)/N))

for i in range(N):
    plt.plot(tList,radialPos[i::N])
plt.xlabel('t'); plt.ylabel('Radial Position');
plt.show()
for i in range(N):
    plt.plot(tList, radialV[i::N])
plt.xlabel('t'); plt.ylabel('Radial Velocity');
plt.show()

radialDist0 = []; radialDist1 = []; radialDist2 = []; radialDist3 = [];
xList0,yList0,xList1,yList1,xList2,yList2,xList3,yList3=[],[],[],[],[],[],[],[]
def plotSnapshot(radialDist, xl, yl, t):
    for i in range(N):
        radialDist.append(np.log(radialPos[int(t/timestep)*N + i]))
        xl.append(xList[int(t/timestep)*N + i])
        yl.append(yList[int(t/timestep)*N + i])
    plt.hist(radialDist, color='blue', edgecolor='black',bins = int(N/4), log=True)
    plt.xlabel('Log(Radial Distance)'); plt.ylabel('Log(Number of particles)')
    plt.show()
    plt.scatter(xl,yl,s=5)
    plt.xlabel('X'); plt.ylabel('Y'); plt.show()

plotSnapshot(radialDist0,xList0,yList0,trelax/2)
plotSnapshot(radialDist1,xList1,yList1,trelax)
plotSnapshot(radialDist2,xList2,yList2,3*trelax/2)
plotSnapshot(radialDist3,xList3,yList3,2*trelax)
