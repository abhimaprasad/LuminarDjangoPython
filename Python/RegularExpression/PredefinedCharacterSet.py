import re

# predefined character sets
# x="[a,b,c]" it will check either a,b,c is present in the string
# x="[a,b,c]"
# x="[a-z]"
# x="[a-z]" it will check all lowercase characters from ato z in string
# x="[0-9]"
#it will check for digits
# x="[A-Z]"
# x="[a-zA-Z0-9]"
# x="[^a-zA-Z0-9]"
# # x="[^a-zA-Z0-9]"EXpect all these return everything
# x="[^0-9]"
# predifned characters
#x= "\s"#(check for space)
# x= "\d"#(check for digit)equivalent to x="[0-9]"
# x="\D"(EXCEPT DIGIT PRINT ALL CHARACTERS x="[0-9]")
# x="\w"(expect special charters x="[a-zA-Z0-9]")
# x="\W"   EQUIVALENT TO  x="[^a-zA-Z0-9]"
x="\W"
matcher=re.finditer(x,"ab7 ABcbk@l")
for match in matcher:
    print(match.start())
    print(match.group())
