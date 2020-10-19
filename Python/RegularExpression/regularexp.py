# pattern matching
string="ababababbbbbababa"
# count number of ab in a given string
# STEP 1:import re
import re
pattern="ab"
matcher=re.finditer(pattern,string)
count=0
# for match in matcher:
#     count+=1
# print(count)
# for match in matcher:
#     print(match.start())
    # (match.start())#it will return position of ab in the string
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)



