class book:
    def __init__(self,pages):
        self.pages=pages

    def __str__(self):
        return str(self.pages)

    def __add__(self, other):
        return book(self.pages+other.pages)

    def __sub__(self, other):
        return self.pages-other.pages

    def __mul__(self, other):
        return self.pages *other.pages

    def __truediv__(self, other):
        return self.pages /other.pages



obj=book(200)
print(obj)
obj1=book(100)
obj2=book(400)
print(obj1)
print(obj+obj1)
print(obj-obj1)
print(obj*obj1 )
print(obj/obj1 )
print(obj+obj1+obj2)
# obj+obj1=300 (int value+obj2(book type))so convert the add to book type

# + operator is used for integer addition and string concatenation
