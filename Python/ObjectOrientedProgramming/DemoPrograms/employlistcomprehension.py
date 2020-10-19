
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

name=[obj.name for obj in li if obj.designation=="developer"]
print(name)

upper=[obj.name.upper() for obj in li]
print(upper)

total=sum(obj.salary for obj in li)
print(total)

maximumsalary=max(obj.salary for obj in li)
print(maximumsalary)