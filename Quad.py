from Vector import *
from Particle import *
class Quad:
    def __init__(self, len, pos, pList):
        self.subquads = []
        self.len = len
        self.pos = pos
        self.pList = pList
        self.computeMass()
        self.computeCOM()

    def getLen(self):
        return self.len

    def getPos(self):
        return self.pos

    def getMass(self):
        return self.mass

    def getCOM(self):
        return self.com

    def computeMass(self):
        m = 0
        for p in self.pList:
            m += Particle.getMass(p)
        self.mass = m

    def computeCOM(self):
        if len(self.subquads) == 0 and len(self.pList) == 0:
            self.com = self.pos
        elif len(self.subquads) == 0:
            vec = Vector([0,0])
            mtot = 0
            for p in self.pList:
                vec += p.mass * p.pos
                mtot += p.mass
            self.com = vec / mtot
        else:
            vec = Vector([0,0])
            mtot = 0
            for q in self.subquads:
                vec += q.mass * q.com
                mtot += q.mass
            self.com = vec / mtot

    def addSubQuads(self):
        p1, p2, p3, p4 = [],[],[],[]
        for p in self.pList:
            if p.inSquare(self.pos+Vector([-self.len/4,-self.len/4]), self.len/2):
                p1.append(p)
            elif p.inSquare(self.pos+Vector([-self.len/4,self.len/4]), self.len/2):
                p2.append(p)
            elif p.inSquare(self.pos+Vector([self.len/4,-self.len/4]), self.len/2):
                p3.append(p)
            elif p.inSquare(self.pos+Vector([self.len/4,self.len/4]),self.len/2):
                p4.append(p)
        self.subquads.append(Quad(self.len/2, self.pos+Vector([-self.len/4,-self.len/4]),p1))
        self.subquads.append(Quad(self.len/2, self.pos+Vector([-self.len/4,self.len/4]),p2))
        self.subquads.append(Quad(self.len/2, self.pos+Vector([self.len/4,-self.len/4]),p3))
        self.subquads.append(Quad(self.len/2, self.pos+Vector([self.len/4,self.len/4]),p4))

    def subqlist(self, qlist):
        qlist.append(self)
        for q in self.subquads:
            q.subqlist(qlist)

    def numQBelow(self):
        num = 0
        if len(self.subquads) == 0:
            return num
        num+=4
        for q in self.subquads:
            num += q.numQBelow()
        return num
