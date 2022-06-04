def search(alist,item):            
    pos=0
    found=False
    stop=False
    while pos<len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
            print("element foundin postons")
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos=pos+1
    return found

a=[]
n=int(input("enter upper limit:-"))
for i in range(0,n):
    e=int(input("enter the element:-"))
    a.append(e)
    x=int(input("enter element to search"))
    search(a,x)