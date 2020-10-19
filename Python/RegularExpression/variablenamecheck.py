# first character should be an alphabet from a to k
# second character must be a number which is divivble by 3
# following by any number of words
# string=a6ght valid
# string=l6ght invalid
import re
rule="[a-k][369][a-z0-9]*"
pattern=input("Enter a string")
match=re.fullmatch(rule,pattern)
if(match==None):
    print("invalid variable name")
else:
    print("valid variable name")