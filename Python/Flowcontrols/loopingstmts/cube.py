Num= int(input("Enter a Number: "))
sum = 0
while(Num!=0):
    Rem = Num % 10
    sum= (sum) + Rem
    Num = Num // 10
print(sum)
