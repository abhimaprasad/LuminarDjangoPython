size=int(input("enter size"))
stack=[]
top=0

def push(element):
    global top
    if top>=(size-1):
        print("stack is full")
    else:
        stack.append(element)
        top=top+1


def pop():
    global top
    print("inside pop")
    if top <= 0:
        print("stack is empty")
    else:
        top = top - 1
        print(top)
        print(stack[top],)

def display():
    print("inside display")
    for i in range(0,top):
        print(stack[i])


n=1
while(n!=0):
    option= int(input("enter the operation 1)Push 2)pop 3)display"))
    if(option==1):
        element=int(input("enter element to push"))
        push(element)
    if (option == 2):
        element = int(input("enter element to pop"))
        pop()
    if (option == 3):
        display()
    n=int(input("u do u want to continue press 0 for exit 1 for continue"))


# proceduretop>0
# size-->3
# case 1:push element
#   1check the stack is full
#   if(top>size)-->stack full
#  else-->stack[top]<--element
#   top=top+1
# pop()
# check for stack is empty
# if(top<=0)

