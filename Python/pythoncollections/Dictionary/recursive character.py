text="ABABCCC"
dict={}
for character in text:
    if(character not in dict):
        dict[character]=1
    else:
        print(character,"is the first character")
        break

