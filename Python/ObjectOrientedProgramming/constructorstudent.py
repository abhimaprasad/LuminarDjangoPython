class student:
    collegename="TOCH"
    def __init__(self,rollno,name,total):
        self.rollno=rollno
        self.name=name
        self.total=total

    def printvalue(self):
        print("The roll no is",self.rollno)
        print("My name is",self.name)
        print("Total is",self.total)
        print("college name is",student.collegename)

s=student(1,"abhima",100)
s.printvalue()