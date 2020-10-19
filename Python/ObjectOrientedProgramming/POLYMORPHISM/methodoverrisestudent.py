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
    def __str__(self):
        return str(self.rollno)+"    "+self.name+"      "+str(self.total)

s=student(1,"abhima",100)
s1=student(2,"abhi",99)
print(s)
print(s1)
#HERE WE ARE PRINTING OBJECT __str__(self) toString() method(PRINT HEXADECIMAL VALUE
#OBJECT CLASS ACT AS THE PARENT CLASS OF ALL CLASSES BY DEFAULT