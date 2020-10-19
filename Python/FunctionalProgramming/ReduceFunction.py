from functools import *
num=[1,2,3,4,5]
total=reduce(lambda num1,num2:num1+num2,num)
print(total)

max=reduce(lambda num1,num2:num1 if num1>num2 else num2,num)
print(max)
