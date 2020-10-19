class parent1:
    def m1(self):
        print("inside parent1 class")
class parent2:
    def m1(self):
        print("inside parent2 class")
class child(parent1,parent2):
    def m3(self):
        print("inside subclass child")
c=child()
c.m3()
c.m1()