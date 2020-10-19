list1=[1,2,3,4,8]
list2=[5,7,8,9]
# li=[]
# for i in list1:
#     for j in list2:
#         li.append((i,j))
# print(li)

output=[(i,j) for i in list1 for j in list2]
print(output)

square=[(i*i) for i in list1]
print(square)

even=[i for i in list1 if i % 2 == 0]
print(even)

out=[i+1 if i<5 else i-1 for i in list1]
print(out)