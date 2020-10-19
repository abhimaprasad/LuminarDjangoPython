employees=[
    [100,"abhi",25000],
    [101,"abhima",22000],
    [102,"abhija",21000],
    [103,"abhila",27000]]

# program to print
for data in employees:
    print(data[1])
# calculate sum of salary
total=0
for data in employees:
    total=total+data[2]
print(total)
#print all employee who have salary greater than 250000
value=25000
for data in employees:
    if(data[2]>value):
        print(data[1])
# print least +ve missig integer
# [-1,0,2,3,4]=>1
# [-1,0,2,3]=>4
