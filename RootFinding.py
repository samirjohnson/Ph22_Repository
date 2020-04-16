import matplotlib.pyplot as plt
import math

def Bisection(func, x1, x2, tol, iter):
    iter+=1
    bracket = (x1, x2)
    x0 = (x1 + x2) / 2
    if func(x0) / func(x1) > 0:
        bracket = (x0, x2)
    else:
        bracket = (x1, x0)
    if abs(func(x0)) < tol:
        return (x0, iter)
    else:
        return Bisection(func, bracket[0], bracket[1], tol, iter)

def NewtonRaphson(func, dfunc, x1, tol, iter):
    iter+=1
    x2 = x1 - func(x1) / dfunc(x1)
    if abs(func(x2)) < tol:
        return (x2, iter)
    else:
        return NewtonRaphson(func, dfunc, x2, tol, iter)

def Secant(func, x1, x2, tol, iter):
    iter+=1
    x3 = x2 - func(x2) * (x2 - x1) / (func(x2) - func(x1))
    if abs(func(x3)) < tol:
        return (x3, iter)
    else:
        return Secant(func, x2, x3, tol, iter)

ZERO = math.pi / 4
f = lambda x: math.sin(x) - 1 / (2) ** (1/2)
df = lambda x: math.cos(x)

LOWERGUESS = 0; UPPERGUESS = 1;
errorListB = []; errorListNR = []; errorListS = [];
iterListB = []; iterListNR = []; iterListS = [];
for i in range(1,15):
    BTup = Bisection(f,LOWERGUESS,UPPERGUESS,10 ** (-i),0)
    NRTup = NewtonRaphson(f,df,UPPERGUESS,10 ** (-i),0)
    STup = Secant(f,LOWERGUESS,UPPERGUESS,10 ** (-i),0)
    errorListB.append(-math.log(abs(BTup[0]-ZERO),2)); iterListB.append(BTup[1]);
    errorListNR.append(-math.log(abs(NRTup[0]-ZERO),2)); iterListNR.append(NRTup[1]);
    errorListS.append(-math.log(abs(STup[0]-ZERO),2)); iterListS.append(STup[1]);

plt.plot(iterListB, errorListB)
plt.show()

plt.plot(iterListNR, errorListNR)
plt.show()

plt.plot(iterListS, errorListS)
plt.show()
