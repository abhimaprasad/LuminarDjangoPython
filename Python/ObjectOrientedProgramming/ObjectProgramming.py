# class
# plan,design,blueprint

# object
# realworld entity

# reference
# tv
# mi tv4
# remote for change sound
# reference is the remote


# Encapsulation
# wraping methods and member functions


# class classname:
    # methods
# object syntax

# referencename=classname()

# self is a keyword to point current object intsnace variable

class Person:
    def setvalues(self,na,ag):
       self.name=na
       self.age=ag

    def printvalues(self):
        print("name is",self.name)
        print("Age is ",self.age)

obj=Person()
obj.setvalues("a",20)
obj.printvalues()