#Callenge13

#1
class Rectangle:
    def __init__(self,h,w):
        self.height = h
        self.width = w
    def calculate_perimeter(self):
        return self.height*2 + self.width*2

class Square:
    def __init__(self,x):
        self.x = x

    def calculate_perimeter(self):
        return self.x * 4

    def change_size(self,p):
        self.x += p

kakukei = Rectangle(9,8)
seihoukei = Square(9)

print(kakukei.calculate_perimeter())
print(seihoukei.calculate_perimeter())

#2
seihoukei.change_size(-5)
print(seihoukei.calculate_perimeter())

#3
class Shape:
    def what_am_i(self):
        print('I am a shape.')

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

r = Rectangle()
s = Square()
r.what_am_i()
s.what_am_i()

#4
class Horse:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self,name):
        self.name = name

r = Rider('chubei')
h = Horse('Makibaoh','unko',r)


print(h.owner.name)
