file=open("Complete.csv","r")
dic={}

for lines in file:
    # print(lines)
    # break
    data=lines.rstrip("\n").split(",")
    state=data[1]
    case=float(data[4])
    if state not in dic:
        dic[state]=case
    else:
        dic[state]=case
# print(dic)
list=[]
# for k,v in dic.items():
#     print(k,",",v)
for k,v in dic.items():
    list.append((v,k))
list=sorted(list,reverse=True)
print(list[0])
