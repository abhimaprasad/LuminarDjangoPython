# kl88bn1375
import re
vehicle=input("enter vehicle registration number")
rule="kl\d{2}\D{2}\d{4}"
rule="kl\d{2}\D{1,2}\d{4}"
match=re.fullmatch(rule,vehicle)
if(match==None):
    print("invalid")
else:
    print("valid")
