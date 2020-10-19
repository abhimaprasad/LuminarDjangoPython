file=open("wordcount","r")
dict={}
for lines in file:
    lines=lines.rstrip("\n").split(" ")
    for word in lines:
        word=word.lower()
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)