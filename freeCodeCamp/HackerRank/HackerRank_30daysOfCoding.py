##Day 2 -- operators
#!/bin/python3

import math
import os
import random
import re
import sys


meal_cost = float(input())

tip_percent = float(input())

tax_percent = float(input())


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    return (meal_cost + (meal_cost*(20/100)) + (meal_cost*(8/100)))

meal_price = solve(meal_cost, tip_percent, tax_percent)
print(float(meal_price))

#############Day 3 - Conditions


###############Day 4 - Class vs Instance
class Person:
    age = 0
    def __init__(self,initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
        else:
            self.age=initialAge

    def amIOld(self):

        if self.age< 13:
            print('You are young')
        elif 13<= self.age < 18:
            print('You are teenager')
        else:
            print('You are old')

    def yearPasses(self):
        self.age = self.age + 1
        return self.age

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

##############Day 5--loops
n = int(input())

for i in range(1,11):
    print('{} X {} = {}'.format(n,i,n*i))


##############Day 6 - Review loop
import math
import os
import random
import re
import sys

n = int(input())
#String = list(map(str, input("").split(" ")))

String = []

for i in range(0,n):
    enterStr = str(input())
    String.append(enterStr)
    #print(enterStr)

#print(str(String))



#print(len(String))
newList =[]
evenList =[]
oddList = []

for i in range(len(String)):
    newList = String[i]
    #print(newList)
    #print(list(newList))
    # now take chracter grouping based on position
    evenList = newList[::2]
    oddList = newList[1::2]
    print(str(evenList) +" "+ str(oddList))

#############Day 7 - Array
#!/bin/python3

import math
import os
import random
import re
import sys
import array
# n = int(input())
# #arr = list(map(int, input().rstrip().split()))
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# print(arr)
# rarr = arr[::-1]
# str1 = ""
# fullString = str1.join([str(ele) in elem in rarr])
# print(fullString)
#

N = input()
A = [int(x) for x in input().split()]
print (' '.join([str(x) for x in reversed(A)]))



#day 8 - Dict & Maps
n = int(input())
d = dict()

for i in range(0, n):
    name, number = input().split()
    d[name] = number
#print(d) Check if your dictionary  is ready

for i in range(0, n):
    name = input()
    if name in d:
        print(f'{name}={d[name]}')
    else:
        print("Not found")

#(OR)

while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else : print("Not found")
    except: break












