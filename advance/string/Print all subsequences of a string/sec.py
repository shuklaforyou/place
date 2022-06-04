def pssr(str, n ,index=-1,curr=""):
    if index==n:
        return 
    if len(curr)>0:
        print(curr,end=" ")
    i=index+1
    while i<n:
        curr=curr+str[i]
        pssr(str,n,i,curr)
        curr=curr[0:-1]
        i=i+1

def pss(str):
    pssr(str,len(str))

str="cab"
pss(str)