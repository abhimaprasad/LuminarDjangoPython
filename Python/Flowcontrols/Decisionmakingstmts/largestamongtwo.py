#read two numbers and print maximum among two numbers
a=int(input("enter a number"))
b=int(input("enter a number"))
if(a>b):
    print("a is greater",a)
elif(b>a):
    print("b is greater",b)
elif(a==b):
    print("both are same")