# how to define dictionary
# dict={}
# values stored in dictionary in the form of key value pairs
# we can store same and different type of data
# duplicates
# duplicate key is not allowed
# duplicate value is allowed
employee={"id":101,"name":"Abhi","salary":20000}
print(employee)
# if we want to acess any value we have to use corresponding key
# print all employeee names
print(employee["name"])
print(employee["salary"])
# updation
# dictionary[key]="value"
# gender:male
employee["gender"]="male"
print(employee)
# update salary as 30000
employee["salary"]+=10000
print(employee)

# checking for a specific key
print("designation" in employee)
print("gender" in employee)