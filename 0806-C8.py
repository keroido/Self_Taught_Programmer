#Challenge8

#1
"""
import random
for i in range(10):
    i = random.randint(1,100)
    print(i)
#ランダムな整数を１０個作る
"""

import statistics

data = [41,47,88,96,15,21,84,68,11,49]
print(statistics.mean(data))

print(statistics.harmonic_mean(data))

print(statistics.median(data))

#2
import cubed

print(cubed.cube(3))

