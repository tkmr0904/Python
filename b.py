import sys, os
from mypkg import *
from math import sqrt


class Point:
    num = 0
    print(list(locals().items()))

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.f = sqrt
        
    
    def pnt(self):
        print(self.x, self.y)

    def distsnce(self, p2 = None):
        if not p2:
            return sqrt(self.x**2 + self.y**2)
        else:
            return sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

    @classmethod
    def class_method(cls):
        print(cls.num)
        

p1 = Point(1, 2)
p2 = Point(2, 1)

p1.pnt()

print(p1.f(400))

Point.class_method()