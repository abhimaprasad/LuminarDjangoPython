file=open("movies.csv","r")
dict={}
count=0
for words in file:
    # 1,The Nightmare Before Christmas,1993,3.9,4568
    movies=words.rstrip("\n").split(",")
    # print(movies)
    # break
    count+=1
    print(count)
    year=movies[2]
    if(year not in dict): #suppose assume 1991 is not in dictorany add it and make count as 1 else incremen count
        dict[year]=1
    else:
        dict[year]+=1
print(dict)
list=[]
for key,value in dict.items():
    list.append((value,key))
srt=sorted(list,reverse=True)
print(srt[0])



# list=[(10,1),(9,2),(3,8),(11,8)]
# sortedlist=sorted(list,reverse=True)
# print(sortedlist)





