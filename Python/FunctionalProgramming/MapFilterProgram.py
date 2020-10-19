# map,filter,reduce
# map function two argumewnts(function,iterable)
# names=["abhi","abhija","abhima"]
#  map -->to select to all name
# filter --->select names that start with apahabet A as an example

# def square(num):
#     return num*num
numbers=[1,2,3,4,5]
# data=list(map(square,numbers))
# print(data)
data=list(map(lambda num:num*num,numbers))
print(data)
# filter even numbers from a list

# def even(num):
#     return num% 2 == 0
# data=list(filter(even,numbers))
# print(data)
data=list(filter(lambda num:num% 2 == 0,numbers))
print(data)