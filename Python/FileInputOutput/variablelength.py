# variable length argument numbers
# def add(num1,num2):
#     return  num1+num2
# only two numbers can be added
# for infinite number use asterik sign and they will be considered as a tuple

# def add(*numbers):
#     print(sum(numbers))
#
# add(10,20,30,40)

# def person(*data):
#     print(data)
#
# person("abhi","kakanad","4000","hello")

# we cannot relate the above data
def person(**args):
    print(args)
    print(type(args))
person(name="abhi",age=20,place="maMALSEERY")