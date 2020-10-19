# create a student with key rollno,name,total

student={"roll no":1,"name":"Abhi","total":50}
# print(student)
print(student["name"])
print("collage" in student)
student["collage"]="luminar technolab"
# print(student)
student["total"]+=50
print(student)

for key in student:
    print(key,",",student[key])