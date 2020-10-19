Num= int(input("Enter a Number: "))
Rev= 0
while(Num!=0):
    Rem = Num % 10
    Rev = (Rev * 10) + Rem
    Num = Num // 10
print(Rev)
