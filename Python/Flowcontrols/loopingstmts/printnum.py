#print numbers beteewn low limit and upper limit

low =int(input("enter lower limit"))
upper=int(input("enter upperlimit"))
if (low>upper):
    print("upp limit should be greater thanlower limit")
while(low<=upper):
    print(low)
    low+=15