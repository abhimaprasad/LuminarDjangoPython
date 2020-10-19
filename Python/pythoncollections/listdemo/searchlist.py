list=[1,2,3,4,5,7,8,9,10]
key=int(input("enter search element"))
flag=0
for x in list:
    if list==key:
        flag=1
        break
    else:
        flag=0
if(flag>0):
    print("element found")
else:
    print("not found")