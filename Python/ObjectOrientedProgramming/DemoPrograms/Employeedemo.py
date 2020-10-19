from functools import *


class Employee:
    def __init__(self, employid, name, salary, experience, designation):
        self.id = employid
        self.name = name
        self.salary = salary
        self.experience = experience
        self.designation = designation

    def printstudent(self):
        print("The employ id is ", self.id)
        print("The NAME IS", self.name)
        print("the salary is", self.salary)
        print("the experience ", self.experience)
        print("he designation is", self.designation)

    def __str__(self):
        return self.name


li = []
file = open("EmpFile", "r")
for line in file:
    data = line.rstrip("\n").split(",")
    print(data)
    id = data[0]
    name = data[1]
    salary = int(data[2])
    experience = data[3]
    designation = data[4]
    obj = Employee(id, name, salary, experience, designation)
    li.append(obj)

# list all employee whose designation is developer
#
# position="developer"
# for obj in li:
#     if obj.designation==position:
#         print(obj.name)
data = list(filter(lambda obj: obj.designation == "developer", li))
for each in data:
    print(each)
# convert all employee names to upper case

data = list(map(lambda obj: obj.name.upper(), li))
print(data)

data1 = reduce(lambda salary1, salary2: salary1 if salary1 > salary2 else salary2,
               list(map(lambda obj: obj.salary, li)))
print(data1)

total = reduce(lambda salary1, salary2: salary1+salary2, list(map(lambda obj: obj.salary, li)))
print(total)

# list all employee whose designation is developer
# convert all employee names to upper case
# find total salary of all employees-->reduce
# find highest salary from an employe--->reduce
