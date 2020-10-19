# parent-child
# base class -derived class
# superclass-subclass

class parent:
    def mobile(self):
        print("i have nokia 5745")
class child(parent):
    def mobile(self):
        print("i have poco x2")
c=child()
c.mobile()