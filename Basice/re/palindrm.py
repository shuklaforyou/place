def nextsmallerElement(arr,n):
        #code here
        #code here
        stack = []
        ans = []
        for ele in arr[::-1]:
            while len(stack)!=0 and stack[-1] > ele:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(ele)
        return print(ans[::-1])

arr=[4,5,2,10,8]
nextsmallerElement(arr,5)