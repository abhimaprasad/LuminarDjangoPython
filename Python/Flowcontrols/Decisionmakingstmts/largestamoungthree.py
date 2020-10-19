num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if((num1>num2)&(num1>num3)):
    print("num1 is greater",num1)
elif((num2>num1)&(num2>num3)):
    print("num2 is greater",num2)
elif((num3>num1)&(num3>num1)):
    print("num3 is large.",num3)
elif((num1==num2) & (num1==num3)):
    print("all are same")