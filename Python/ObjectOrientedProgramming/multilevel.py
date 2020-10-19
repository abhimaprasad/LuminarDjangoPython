class Parent:
    def m1(self):
        print("inside parent class")
class child(Parent):
    def m2(self):
        print("insisde child class")

class subchild(child):
    def m3(self):
        print("inside subchild subclass")

sub=subchild()
sub.m3()
sub.m2()
sub.m1()