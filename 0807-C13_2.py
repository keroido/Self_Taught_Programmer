class Shape():
    def what_am_i(self):
        print('I am a shape.')

class Rectangle(Shape):
    def __init__(self,h,w):
        self.height = h
        self.width = w
    def calculate_perimeter(self):
        return self.height*2 + self.width*2

class Square(Shape):
    def __init__(self,x):
        self.x = x

    def calculate_perimeter(self):
        return self.x * 4

    def change_size(self,p):
        self.x += p

a = Rectangle(9,8)
b = Square(5)

a.what_am_i()
b.what_am_i()
