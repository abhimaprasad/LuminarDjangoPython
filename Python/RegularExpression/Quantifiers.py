from re import *

pattern="aaaabaabababababababaaaaba"
# x="a+"# it will check for single A and sequence of a
# x="a*" it will also check the space of b
# x="a?" minimum one time
# x="^a" given pattern starting with a
# x="a$"#is the given pattern end with a
# x="a{2}" it willl check for two aa
# x="a{2,3}" minium 2 a and maximum 3 a
matcher=finditer(x,pattern)
for match in matcher:
    print(match.start())
    print(match.group())