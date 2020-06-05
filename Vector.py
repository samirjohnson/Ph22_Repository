import math
class Vector(list):

    def __add__(self, other):
        try:
            return Vector(map(lambda x,y: x+y, self, other))
        except TypeError:
            return Vector(map(lambda x: x + other, self))

    def __neg__(self):
        return Vector(map(lambda x: -x, self))

    def __sub__(self, other):
        try:
            return Vector(map(lambda x,y: x - y, self, other))
        except TypeError:
            return Vector(map(lambda x: x - other, self))

    def __mul__(self, other):
        try:
            return Vector(map(lambda x,y: x * y, self, other))
        except TypeError:
            return Vector(map(lambda x: x * other, self))

    def __truediv__(self, other):
        try:
            return Vector(map(lambda x,y: x / y, self, other))
        except TypeError:
            return Vector(map(lambda x: x / other, self))

    def __radd__(self, other):
        try:
            return Vector(map(lambda x,y: x + y, other, self))
        except TypeError:
            return Vector(map(lambda x: other + x, self))

    def __rsub__(self, other):
        try:
            return Vector(map(lambda x,y: x - y, other, self))
        except TypeError:
            return Vector(map(lambda x: other - x, self))

    def __rmul__(self, other):
        try:
            return Vector(map(lambda x,y: x * y, self, other))
        except TypeError:
            return Vector(map(lambda x: x * other, self))

    def __rdiv__(self, other):
        try:
            return Vector(map(lambda x,y: x / y, other, self))
        except TypeError:
            return Vector(map(lambda x: other / x, self))

    def __iadd__(self, other):
        try:
            return self + other
        except:
            return

    def magnitude(self):
        try:
            mag = 0
            for i in self:
                mag += i**2
            return math.sqrt(mag)
        except:
            return

    def crossProduct(self, other):
        try:
            if (len(self) == 3):
                x = self[1]*other[2] - self[2]*other[1]
                y = self[2]*other[0] - self[0]*other[2]
                z = self[0]*other[1] - self[1]*other[0]
                return Vector([x,y,z])
            else:
                return self[0]*other[1] - self[1]*other[0]
        except:
            return
