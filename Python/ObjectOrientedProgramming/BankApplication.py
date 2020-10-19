import datetime
class Bank:
    bankname="canara"
    def createaccount(self,accno,personname):
        self.accno=accno;
        self.personmane=personname

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
b.createaccount(101001,"abhi")
b.widrawal(100000)
b.deposit(20000)
b.balanceenquiry()

# different types of variable
# instance varaiable- is always related to object(self keyword)
# static variable can be accessed by using class name
# static is a keyword used for efficient memeory use