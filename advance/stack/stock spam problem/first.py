
def ssp(arr):
    n=len(arr)-1
    stack=[]
    ans=[]
    rearr=arr[::-1]
    for ele,index in enumerate(rearr):
        while len(stack)!=0 and stack[-1][0] < arr[ele]:
            stack.pop()
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1][1])
        stack.append([index,ele])
    
    for k in range(len(ans)):
        ans[k]=k-ans[k]
    
    return print(ans)


arr=[100,80,60,70,60,75,85]
ssp(arr)
        