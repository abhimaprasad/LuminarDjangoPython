file=open("Info","r")
list=[]
listlower=[]
for lines in file:
    line = lines.rstrip("\n")
    words=line.split(" ")
    for i in words:
        list.append(i.upper())
        listlower.append(i.lower())
print(list)
print(listlower)
