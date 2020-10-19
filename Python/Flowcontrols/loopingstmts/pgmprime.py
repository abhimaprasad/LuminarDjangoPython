# num= int(input("Enter a Number: "))
# count=0
# for i in range(1,num+1):
#     if (num % i) == 0:
#         count=count+1;
# if(count==2):
#     print("prime")
# else:
#         print("not a prime number")
num= int(input("Enter a Number: "))
flag=0
for i in range(2,num):
    if (num % i) == 0:
        flag=1
        break
    else:
        flag=0
if(flag>0):
        print("not a prime number")
else:
    print("prime")

