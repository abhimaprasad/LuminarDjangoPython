list=[-1,0,1,2,4]
count=1
for i in range(0,len(list)):
    if(count in list):
        pass
    else:
        print(count,"is the +ve missing integer")
        break
    count+=1