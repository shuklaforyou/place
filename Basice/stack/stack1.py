stack=[]
def push():
    element=input("enter the element!")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is emnpty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)

while True:
    print("select the operation 1.push 2.pop 3,quit")
    choise=int(input())
    if choise==1:
        push()
    elif choise==2:
        pop()
    elif choise==3:
        break
    else:
        print("Enter the correct operations")