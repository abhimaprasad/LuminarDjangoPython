class Employee:
    cname="toch"
    def __init__(self,id,design,salary):# def setEmpolyee(self,id,design,salary):
        self.id=id
        self.designation=design
        self.salary=salary

    def printEmpolyee(self):
        print("the id is",self.id)
        print("the designation is",self.designation)
        print("salary is",self.salary)
        print("company name is",Employee.cname)
emp=Employee(1,"doctor",50000)
emp.printEmpolyee()
# emp.setEmpolyee(1,"doctor",50000)
# emp.printEmpolyee()


# setemployee method is used for intialaizing
# printemployee for printing instance variable


# constructor

# to intialaize instance variable(same use of setemployye)
# constructor name is always  __init__
