class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(a,n,b,m):
          for i in range(m):
           a.append(b[i])
           print(a,"i",i)
          return len(set(a))
        #code here

    if __name__=="__main__":
        # n,m=map(int,input().split())
        # a=list(map(int,input().split()))
        # b=list(map(int,input().split()))
        n=4
        m=3
        a=[1,2,3,4]
        b=[1,2,3]
        print(doUnion(a,n,b,m))