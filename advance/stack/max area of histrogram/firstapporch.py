
def nsl(arr):
    stack=[]
    left=[]
    for i in range(len(arr)):
        while len(stack)!=0 and stack[-1][0] > arr[i]:
            stack.pop()
        if len(stack)==0:
            left.append(-1)
        else:
            left.append(stack[-1][1])
        stack.append([arr[i],i])
    
    # for k in range(len(left)):
    #     left[k]=k-left[k]
    
    return left

def nsr(arr):
    stack=[]
    right=[]
    for ele in arr[::-1]:
        while len(stack)!=0 and stack[-1][0] > ele:
            stack.pop()
        if len(stack)==0:
            right.append(7)
        else:
            right.append(stack[-1][1])
        stack.append([ele,arr.index(ele)])
    
    # for k in range(len(right)):
    #     right[k]=k-right[k]
    
    return right[::-1]


arr=[6,2,5,4,5,1,6]
right1 = nsr(arr)
left2 = nsl(arr)
widtharr=[]
finalarr=[]
maxint=-10
for i  in range(len(arr)):
    widtharr.append(right1[i]-left2[i]-1)
# for i in range(len(arr)):
    finalarr.append(arr[i]*widtharr[i])
    maxint=max(maxint,finalarr[i])
# for i in range(len(finalarr)):
#     maxint=max(maxint,finalarr[i])
print(maxint)