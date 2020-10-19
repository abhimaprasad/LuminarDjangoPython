file=open("Employee","r")
employe={}

for lines in file:
        line = lines.rstrip("\n").split(",")
        print(line)
        id=line[0]
        name=line[1]
        salary=line[2]
        experience=line[3]
        designation =line[4]
        if id not in employe:
            employe[id]={"id":id,"name":name,"salary":salary,"experience":experience,"designation":designation}
        else:
            pass
print(employe)









# for k,v in employe.items():
#     print(k,"-->",v)
#
# def Employedetails(id):
#     if id in employe:
#         print(employe[id]["name"])
#     else:
#         print("employ doesnot exixt")
#
# Employedetails("1001")
#
# def Employedetails(id):
#     if id in employe:
#         print(employe[id]["salary"])
#     else:
#         print("employ doesnot exixt")
#
# Employedetails("salary")
#
# #
# #
def employeeDetails(**args):
     print(args)
     eid=args["id"]
     print(eid)
     prop = args["prope"]
     # print(prop)
     print(employe[eid]["name"])
     print(employe[eid][prop])

employeeDetails(id="1001",prope="designation")