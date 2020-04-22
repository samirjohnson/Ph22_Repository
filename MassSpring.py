import math
import numpy as np
import matplotlib.pyplot as plt

h = 0.1/16; N = 10;

tVals = np.linspace(0, N, int(N / h + 1))
xVals1 = np.zeros(int(N / h + 1)); vVals1 = np.zeros(int(N / h + 1));
xVals2 = np.zeros(int(N / h + 1)); vVals2 = np.zeros(int(N / h + 1));

X = 0; V = 1;
xVals1[0] = X; vVals1[0] = V; xVals2[0] = X; vVals2[0] = V;
xError1 = [0]; xError2 = [0];
xPos = lambda t: X * math.cos(t) + V * math.sin(t)

for t in tVals:
    i = np.where(tVals==t)[0][0]
    if i != 0:
        xVals1[i] = xVals1[i-1] + h * vVals1[i-1]
        vVals1[i] = vVals1[i-1] - h * xVals1[i-1]
        x1 = h * vVals2[i-1]; x2 = h * (vVals2[i-1] + x1);
        xVals2[i] = xVals2[i-1] + 1/2 * (x1 + x2)
        v1 = h * (-xVals2[i-1]); v2 = -h * (xVals2[i-1] + v1)
        vVals2[i] = vVals2[i-1] + 1/2 * (v1 + v2)
        xError1.append(abs(xVals1[i] - xPos(tVals[i])))
        xError2.append(abs(xVals2[i] - xPos(tVals[i])))

plt.plot(tVals, xError1, label='Explicit Euler Error')
plt.plot(tVals, xError2, label='Improved Euler Error')
plt.xlabel('Time'); plt.ylabel('Error')
plt.legend()
plt.show()
