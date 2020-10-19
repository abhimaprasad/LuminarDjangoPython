file=open("numbers","r")
list=[]
for numbers in file:
    # remove /n**The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
    numbers=int(numbers.rstrip("\n"))
    list.append(numbers)
print(list)
total=sum(list)
print("sum is",total)

minimum=min(list)
print("minimum value is",minimum)

maximum=max(list)
print("maximum value is",maximum)
