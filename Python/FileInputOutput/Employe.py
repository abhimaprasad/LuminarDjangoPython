file=open("Employee","r")
listname=[]
listsalary=[]
for lines in file:
    line=lines.rstrip("\n")
    data=line.split(",")
    name=data[1]
    salary=data[2]
    listname.append(name)
    listsalary.append(salary)
print(listname)
print(listsalary)

