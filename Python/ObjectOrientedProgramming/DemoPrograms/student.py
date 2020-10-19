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
list=[]
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
    list.append(obj)
# for obj in list:
#     # print all students who have mark greater than 150
#     if obj.total>150:
#         print(obj)
# maximum value of total
total=[]
for obj in list:
    total.append(obj.total)
# print(max(total))
maximum=max(total)
for obj in list:
    if obj.total==maximum:
        print(obj)





