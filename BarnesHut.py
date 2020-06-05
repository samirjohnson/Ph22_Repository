from Quad import *
from Particle import *
from Vector import *
import numpy as np
import random
import matplotlib.pyplot as plt
import time

M = 1; G = 1; R = 1; a = 0.1; N = 100; tdyn = math.sqrt(R**3/(G*M*N));
tfinal = 6*math.pi*tdyn; timestep = 0.005; trelax = N / (10 * math.log(N)) * tdyn;
theta = 0.1

quadlist = []

def createTree(quad):
    if len(quad.pList) <= 1:
        return quad
    else:
        quad.addSubQuads()
        createTree(quad.subquads[0])
        createTree(quad.subquads[1])
        createTree(quad.subquads[2])
        createTree(quad.subquads[3])
        return quad

def evaluateODE(vi, dt, f, tf):
    tlist = np.linspace(0, tf, int(tf/dt)+1)
    pl = [0] * len(tlist); pl[0] = vi;
    for i in range(1,int(tf/dt+1)):
        pl[i] = pl[i-1] + dt * f(pl[i-1], tlist[i-1],dt)
    return pl

def maxDist(pl):
    md = 0
    for p in pl:
        if md < Vector.magnitude(p.pos):
            md = Vector.magnitude(p.pos)
    return md

def updateFunc(pvec, t, dt):
    acc = lambda x1, x2, m: -G * m * (x1 - x2) / (Vector.magnitude(x1 - x2)**(3) + Vector.magnitude(x1 - x2)*a**2)
    pquad = Quad(2*maxDist(pvec), Vector([0,0]), pvec)
    quad = createTree(pquad); quadlist.append(quad);
    retvec = Vector([pvec[0]]*len(pvec))
    for p in pvec:
        force = Vector([0,0])
        qlist = []
        quad.subqlist(qlist)
        index = 0
        while index < len(qlist):
            acc = lambda x1, x2, m: -G * m * (x1 - x2) / (Vector.magnitude(x1 - x2)**(3) + Vector.magnitude(x1 - x2)*a**2)
            if len(qlist[index].pList) == 0:
                index+=1
            elif len(qlist[index].pList) == 1:
                try:
                    force += acc(p.pos, qlist[index].pList[0].pos, qlist[index].mass)
                except ZeroDivisionError:
                    force += Vector([0,0])
                index+=1
            else:
                if qlist[index].len/Vector.magnitude(p.pos - qlist[index].com) < theta:
                    if p.inQuad(qlist[index]):
                        q = qlist[index]
                        force += acc(p.pos, q.com - p.mass*p.pos/q.mass, q.mass-p.mass)
                    else:
                        force += acc(p.pos, qlist[index].com, qlist[index].mass)
                    index += qlist[index].numQBelow()
                else:
                    index+=1
        retvec[pvec.index(p)] = Particle(p.mass, p.vel + dt*force, force);
    return retvec

plist = []
r1 = random; r2 = random; r3 = random; r1.seed(1); r2.seed(2); r3.seed(3);
for i in range(N):
    plist.append(Particle(M, Vector([0,0]), Vector([0,0])))
    theta1 = 2 * math.pi * r1.random(); theta2 = 2 * math.pi * r2.random();
    plist[i].updatePos(r3.random()*R*Vector([math.cos(theta1), math.sin(theta1)]))
    plist[i].updateVel(0.1*Vector.magnitude(plist[i].pos)*Vector([math.cos(theta2),math.sin(theta2)]))

pINIT = Vector(plist)

t1 = time.perf_counter()
pl = evaluateODE(pINIT, timestep, updateFunc, tfinal)
t2 = time.perf_counter()
print('Time to run simulation: {} seconds'.format(t2 - t1))

radialPos, radialVel, totAngMom, xlist, ylist = [], [], [], [], []
for pvec in pl:
    L = 0
    for p in pvec:
        pos = Vector.magnitude(p.pos); vel = Vector.magnitude(p.vel);
        radialPos.append(pos); radialVel.append(vel);
        L += Vector.crossProduct(p.pos, p.mass * p.vel)
        xlist.append(p.pos[0]); ylist.append(p.pos[1]);
    totAngMom.append(L)

tlist = np.linspace(0, tfinal, int(len(radialPos)/N))

for i in range(N):
    plt.plot(tlist, radialPos[i::N])
plt.xlabel('t'); plt.ylabel('Radial position')
plt.show()

plt.plot(tlist, totAngMom)
plt.xlabel('t'); plt.ylabel('Total Angular Momentum')
plt.show()
L0 = totAngMom[0]; LF = totAngMom[len(totAngMom)-1];
print('Initial total angular momentum: ' + str(L0))
print('Final total angular momentum: ' + str(LF))

radialDist0, radialDist1, radialDist2, radialDist3 = [], [], [], []
xList0,yList0,xList1,yList1,xList2,yList2,xList3,yList3=[],[],[],[],[],[],[],[]

def drawQuads(q):
    x = q.pos[0]; y = q.pos[1]; l = q.len/2;
    plt.plot([x-l,x+l], [y+l,y+l],color='black')
    plt.plot([x-l,x+l], [y-l,y-l],color='black')
    plt.plot([x-l,x-l], [y-l,y+l],color='black')
    plt.plot([x+l,x+l], [y-l,y+l],color='black')
    for sq in q.subquads:
        drawQuads(sq)
    return

def plotSnapshot(radialDist, xl, yl, t):
    for i in range(N):
        radialDist.append(np.log(radialPos[int(t/timestep)*N + i]))
        xl.append(xlist[int(t/timestep)*N + i])
        yl.append(ylist[int(t/timestep)*N + i])
    plt.hist(radialDist, color='blue', edgecolor='black',bins = int(N/4), log=True)
    plt.xlabel('Log(Radial Distance)'); plt.ylabel('Log(Number of particles)')
    plt.show()
    plt.scatter(xl,yl,s=5)
    drawQuads(quadlist[int(t/timestep)])
    plt.xlabel('X'); plt.ylabel('Y'); plt.show();

plotSnapshot(radialDist0,xList0,yList0,trelax/2)
plotSnapshot(radialDist1,xList1,yList1,trelax)
plotSnapshot(radialDist2,xList2,yList2,3*trelax/2)
plotSnapshot(radialDist3,xList3,yList3,2*trelax)
