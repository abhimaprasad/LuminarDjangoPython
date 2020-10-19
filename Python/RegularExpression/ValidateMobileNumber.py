import re
number=input("enter mobile number")
# rule="[0-9]{10}"
rule="(91)?\d{10}"
match=re.fullmatch(rule,number)
if(match==None):
    print("Invalid Mobile Number")
else:
    print("Valid Mobile Number")
