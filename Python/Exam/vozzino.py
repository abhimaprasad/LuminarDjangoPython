name="HHHPPSDAAA"
dict={}
for count in name:
    if count not in dict:
        dict[count]=1
    else:
        dict[count]+=1
print(dict)
final=" "
for k,v in dict.items():
    final=final+str(v)+k
print(final)


