class parent:
    def property(self):
        print("gold")
    def boy(self):
        print("marry raman")

class child(parent):
    def boy(self):
        print("marry nivin")

c=child()
c.boy()

