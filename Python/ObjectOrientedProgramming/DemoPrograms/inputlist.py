list=[4,1,2,5,7,8,10]
list1=[]
for element in list:
    if element<5:
        element=element-1
        list1.append(element)
    elif element>5:
        element+=1
        list1.append(element)
print(list1)

