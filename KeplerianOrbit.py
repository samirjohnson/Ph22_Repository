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

tList = np.linspace(0,T,int(T)+1)
xList = []; yList = [];
for t in tList:
    C = NewtonRaphson(eq, deq, GUESS(t), t, tol)
    xList.append(X(C))
    yList.append(Y(C))

plt.plot(xList, yList)
plt.title("Elliptical Keplerian Orbit")
plt.xlabel("X-Coordinate (m)")
plt.ylabel("Y-Coordinate (m)")
plt.show()
