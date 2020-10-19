class Student:


    def setvalue(self,roll,na,course,total):
        self.id=roll
        self.name=na
        self.co=course
        self.full=total

    def printvalue(self):
        print(self.id)
        print(self.name)
        print(self.co)
        print(self.full)

s=Student()
s.setvalue(12,"abhi","cse",150)
s.printvalue()