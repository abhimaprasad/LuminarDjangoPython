# print numbers beteewn low limit and upper limit

low = int(input("enter lower limit"))
upper = int(input("enter upperlimit"))
if (low > upper):
    print("upp limit should be greater thanlower limit")
while (low <= upper):
    if (low % 2 == 0):
        print(low)
    low += 1
