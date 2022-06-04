# t=int(input())
# for i in range(t):
x,y=map(int,input().split())
a=x*10
b=y*5
print(a,b)
if a==b:
    print("ANY")
elif a>b:
    print("FIRST")
elif a<b:
    print("SECOND")