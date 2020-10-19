lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
flag=0
for i in range(lower,upper):
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
        else:
            flag =0
    if(flag==0):
            print(i)



