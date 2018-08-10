#Challenge12

#1
class Apple:
    def __init__(self,w,c,t,s):
        self.weight = w
        self.color = c
        self.taste = t
        self.smell = s

#2
class Circle:
    def area(self,r):
        import math
        self.r = r
        return math.pi * self.r**2

maru = Circle()
print(maru.area(3))

#3
class Triangle:
    def area(self,h,w):
        self.height = h
        self.width = w
        return self.height*self.width/2

sankaku = Triangle()
print(sankaku.area(10,10))

#4
class Hexagon:
    def calculate_perimeter(self,x):
        self.x = x
        return x*6

hexa = Hexagon()
print(hexa.calculate_perimeter(6))
