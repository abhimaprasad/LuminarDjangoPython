# METHOD OVERLOADING
# SAME METHOD NAME BUT DIFFERENT NUMBER OF ARGUMENTS
# PYTHON ONLY SUPPORT RECENTLY IMPLEMENTED METHOD(LAST ONE) FOR METHOD OVERLOADING
class maths:
    def add(self):
        num1,num2=10,20
        print(num1+num2)
    def add(self,num1):
        num2=50
        print(num1+num2)
    # def add(self,num1,num2):
    #     print(num1+num2)

m=maths()
# m.add(10,20)
# m.add()
m.add(10)