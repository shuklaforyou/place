queue=[]
def enqueue():
    element=input("Enter the element")
    queue.append(element)
    print(element,"is added  to queue!")

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("removed element",e)

def display():
    print(queue)

while True:
    print("slected the operation 1.add 2.removed 3.show 4.quit!")
    choise=int(input())
    if choise==1:
        enqueue()
    elif choise==2:
        dequeue()
    elif choise==3:
        display()
    elif choise==4:
        break
    else:
        print("Enter the corrrect operations!")

        