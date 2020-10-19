

list_of_pairs= [(10,4),(90,3),(9,1),(10,4),(9,5)]
list=[]
sum = 0

def fun1():
   for pair in list_of_pairs:
      sum= pair[0]+pair[1]
      list.append(sum)
   print(list)
   return list
list=fun1()
list.sort()
print (list)