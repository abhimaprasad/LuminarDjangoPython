import datetime
class person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print(self.name)
        print(self.age)
class Bank(person):
    bankname="canara"
    def createaccount(self,accno):
        self.accno=accno

        self.balance=1000
    def deposit(self,amount):
        self.balance+=amount
        print("your bank",Bank.bankname,"has been credited with amount",amount,"The avaliable balance is RS:",self.balance)
    def widrawal(self,amount):
        if amount>self.balance:
            print("insuffient balance")
        else:
            self.balance-=amount
            print("your bank", Bank.bankname, "has been credited with amount", amount, "The avaliable balance is RS:",self.balance,"at ",datetime.date.today())
    def balanceenquiry(self):
        print("balance is",self.balance)
b=Bank()
b.setperson("abhi",20)
b.printvalue()
b.createaccount(45558)
b.deposit(5000000)
b.widrawal(45)
b.balanceenquiry()
