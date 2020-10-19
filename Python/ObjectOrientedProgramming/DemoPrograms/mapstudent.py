class student:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total
    def printstudent(self):
        # print(self.roll)
        print(self.name)
        print(self.course)
        print(self.total)

    def __str__(self):
        return self.name
list1=[]
file=open("Student","r")
for lines in file:
    line=lines.rstrip("\n").split(",")
    print(line)
    #['1', 'abhima', 'cs', '400']
    id=line[0]
    name=line[1]
    course=line[2]
    total=int(line[3])
    obj=student(id,name,course,total)
    list1.append(obj)
data=list(map(lambda obj:obj.name.upper(),list1))
print(data)
stud=list(filter(lambda obj:obj.total>450,list1))
for each in stud:
    print(each)




