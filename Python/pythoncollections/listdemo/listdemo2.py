list=[10,11,12,13,14,15,17,18]
# print(list)
# print(list[0])
# print(list[1])

# iteration
# for item in list:
#     print(item)
# sum=0
# for item in list:
#     sum+=item
# print(sum)

# print all even numbers from list

# for item in list:
#     if(item%2==0):
#         print(item)
# find sum of ood and even numbers
evensum=0
oddsum=0
for item in list:
     if(item%2==0):
         evensum=evensum+item
     else:
            oddsum=oddsum+item
print(evensum)
print(oddsum)
        


