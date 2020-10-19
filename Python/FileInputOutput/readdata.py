file=open("words","r")

list=[]
for words in file:
    word=words.rstrip("\n")
    word1=words.split(" ")
    for wrd in word1:
        list.append(wrd)
print(list)
