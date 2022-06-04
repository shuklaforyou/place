# x=list(map(str,input().split()))
# print(x[::-1])
def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l<=r:
            s[l],s[r] = s[r],s[l]
            l +=1
            r -=1
        print(s)


tep=list(map(str,input().split()))
reverseString(tep)