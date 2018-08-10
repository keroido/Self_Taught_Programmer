class Shape():
    def what_am_i(self):
        print('I am a shape.')

class Square(Shape):
    square_list = []
    def __init__(self,x):
        self.x = x
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.x * 4

    def change_size(self,p):
        self.x += p

    def what_am_i(self):
        super().what_am_i()
        print('I am a shape.')

    def __repr__(self):
        return '{} by {} by {} BY {}'.format(self.x,self.x,self.x,self.x)

a = Square(5)
print(a.square_list)
b = Square(8)
print(b.square_list)

square = Square(29)
print(square)


def usohakken(x,y):
    return x is y

print(usohakken(1,2))
