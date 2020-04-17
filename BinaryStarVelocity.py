import matplotlib.pyplot as plt
import math
import numpy as np

def NewtonRaphson(func, dfunc, x1, t, tol):
    x2 = x1 - func(x1,t) / dfunc(x1)
    if abs(func(x2,t)) < tol:
        return x2
    else:
        return NewtonRaphson(func, dfunc, x2, t, tol)

a = 2.34186 * 3 * 10 ** 8; e = 0.617139; T = 27906.98161

eq = lambda C,t: T / (2 * math.pi) * (C - e * math.sin(C)) - t
deq = lambda C: T / (2 * math.pi) * (1 - e * math.cos(C))
X = lambda C: a * (math.cos(C) - e)
Y = lambda C: a * math.sqrt(1 - e ** 2) * math.sin(C)

GUESS = lambda t: 2 * math.pi * t / T; tol = 10 ** (-6)

tList = np.linspace(0,2*T,2*int(T)+1)
xList = []; yList = []; rvList = []; dt = 0.0001; phi = math.pi / 2;
v = lambda x1,x2: (x1 - x2)/dt
dotprod = lambda x1,x2: math.cos(phi) * x1 + math.sin(phi) * x2
for t in tList:
    C = NewtonRaphson(eq, deq, GUESS(t), t, tol)
    xList.append(X(C))
    yList.append(Y(C))
    if t != 0:
        i = np.where(tList==t)[0][0]
        vx = v(xList[i],xList[i-1])/1000
        vy = v(yList[i],yList[i-1])/1000
        rvList.append(-dotprod(vx,vy))

ttList = tList / T
plt.plot(np.delete(ttList,0), rvList)
plt.xlabel("t/T")
plt.ylabel("Radial Velocity (km/s)")
plt.show()
