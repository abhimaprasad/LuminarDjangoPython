list1 = [1,2,3,0,2,3,0,1,24,0,1,3,1,0,1,21,0,1,2,0,45]
list1.sort()
a=list1[1]
b=list1.count((a))
# b=list1.count(2)
print(b)
print(list1[b:]+ list1[:b])
