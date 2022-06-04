l=[]
n=int(input("eneter the upper limit"))
for i in range(0,n):
    a=int(input("enter the number"))
    l.append(a)
    maxno=l[0]
for i in range(0,len(l)):
    if l[i]>maxno:
        maxno=l[i]

print("the maxmimum number is %d"%maxno)