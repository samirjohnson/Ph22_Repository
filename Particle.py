import math
from Vector import *
from Quad import *
class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos = pos
        self.vel = vel

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def getMass(self):
        return self.mass

    def updatePos(self, pos):
        self.pos = pos

    def updateVel(self, vel):
        self.vel = vel

    def dist(self, p1):
        return Vector.magnitude(self.pos - p1.getPos())

    def inSquare(self, center, len):
        return (center[0] - len/2 <= self.pos[0] <= center[0] + len/2) and (center[1] - len/2 <= self.pos[1] <= center[1] + len/2)

    def pforce(self, p1, a, G):
        acc = lambda x1, x2, m: -G * m * (x1 - x2) / (Vector.magnitude(x1 - x2)**(3) + Vector.magnitude(x1 - x2)*a**2)
        try:
            return acc(self.pos, p1.pos, p1.mass)
        except ZeroDivisionError:
            return Vector([0,0])

    def qforce(self, q, a, theta, G):
        if len(q.pList) == 0:
            return Vector([0,0])
        elif len(q.pList) == 1:
            return self.pforce(q.pList[0], a, G)
        else:
            acc = lambda x1, x2, m: -G * m * (x1 - x2) / (Vector.magnitude(x1 - x2)**(3) + Vector.magnitude(x1 - x2)*a**2)
            if q.len / Vector.magnitude(self.pos - q.com) > theta:
                return acc(self.pos, q.com, q.mass)
            else:
                f = Vector([0,0])
                for quad in q.subquads:
                    f += self.qforce(quad, a, theta, G)
                return f

    def inQuad(self, quad):
        return self.inSquare(quad.pos, quad.len)

    def __add__(self, other):
        try:
            return Particle(self.mass, self.pos + other.pos, self.vel + other.vel)
        except TypeError:
            return Particle(self.mass, self.pos + other, self.vel + other)

    def __radd__(self, other):
        try:
            return Particle(self.mass, other.pos + self.pos, other.vel + self.vel)
        except TypeError:
            return Particle(self.mass, other + self.pos, other + self.vel)

    def __sub__(self, other):
        try:
            return Particle(self.mass, self.pos - other.pos, self.vel - other.vel)
        except TypeError:
            return Particle(self.mass, self.pos - other, self.vel - other)

    def __rsub__(self, other):
        try:
            return Particle(self.mass, other.pos - self.pos, other.vel - self.vel)
        except TypeError:
            return Particle(self.mass, other - self.pos, other - self.vel)

    def __mul__(self, other):
        try:
            return Particle(self.mass, self.pos * other, self.vel * other)
        except:
            return

    def __rmul__(self, other):
        try:
            return Particle(self.mass, other * self.pos, other * self.vel)
        except:
            return

    def __truediv__(self, other):
        try:
            return Particle(self.mass, self.pos / other, self.vel / other)
        except:
            return

    def __rdiv__(self, other):
        try:
            return Particle(self.mass, other / self.pos, other / self.vel)
        except:
            return
