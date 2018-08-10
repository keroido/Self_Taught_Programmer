#charenge3

#1
print('coffee')
print('tea')
print('juice')

print('_______________________________________________________________')

#2,3
import random
x = random.randint(0,30)
print(x)
if x < 10:
    print('１０未満')
elif x >= 10 and x < 25:
    print('１０〜２５')
else:
    print('２５以上')
print('_______________________________________________________________')

#4
print(x%2)

print('_______________________________________________________________')

#5

print(x/2)

print('_______________________________________________________________')

#6
age = random.randint(0,100)
print('You are %s years old' % age)
if age < 18:
    print('You can not drink alcohol')
elif age >= 18 and age <= 65:
    print('You are adalts')
else:
    print('You are old')
