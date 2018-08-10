#Charenge4

import random

#1
number = int(input('type a number'))
def f(number):
    print(number**2)

f(number)
print('_______________________________________________________________')

#2
def ps(s):
    print(str(s))
ps('Fuck')
print('_______________________________________________________________')

#3
def fifth(x,y,z,a=1,b=2):
    print((x**y//z*a)/2)

p = random.randint(1,10)
q = random.randint(1,10)
r = random.randint(1,10)
fifth(p,q,r)
print('_______________________________________________________________')

#4

def half(x=random.randint(1,99)):
    return x/2
def count(y):
    return y*4
print(half())
n = half()
z = count(n)
print(z)
print('_______________________________________________________________')

#5
def change(n):
    print(float(n))
    
try:
    change(input('type'))
except ValueError:
    print('could not convert string')
print('_______________________________________________________________')






    
