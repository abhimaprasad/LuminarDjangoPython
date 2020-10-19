s=[1,2,3,4,5,7,8]
print(len(s))
a=[]
def sum(num):
    for i in range(0,len(s)):
        for j in range(i+1, len(s)):
            if(s[i]+s[j]==num):
                p=s[i],s[j]
                a.append(p)
    print(a)

num=int(input("enter a number"))
sum(num)


