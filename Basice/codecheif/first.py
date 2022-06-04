
def even(x,y,b):
    count=0
    while b>=1:
        if b%2==0:
            y+=2
            b-=2
            count+=1
        else:
            x+=1
            b-=1
            count+=1
    print(count)

def oddd(x,y,b):
    count=0
    while b>=0:
        if b%2==0:
            y+=2
            b-=2
            count+=1
        else:
            x+=1
            b-=1
            count+=1
    print(count)

T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    if x<y:
        a=y-x
        print(int(a))
    elif x>y:
        b=x-y
        if b%2==0:
            even(x,y,b)
            
        else:
            oddd(x,y,b)
            
    else:
        print(0)