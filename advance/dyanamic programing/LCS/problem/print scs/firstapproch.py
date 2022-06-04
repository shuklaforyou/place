def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 

    t = [[None]*(n+1) for i in range(m+1)]
 
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                t[i][j] = 0
            elif X[i-1] == Y[j-1]:
                t[i][j] = t[i-1][j-1]+1
                
            else:
                t[i][j] = max(t[i-1][j] , t[i][j-1])
 

    i=m
    j=n
    s=""
    while(i>0 and j >0):
        if (X[i-1]==Y[j-1]):
            s +=(X[i-1])
            i -=1
            j -=1
        else:
            if t[i][j-1]>t[i-1][j]:
                s +=Y[j-1]
                j -=1
            else:
                s +=X[i-1]
                i -=1  
    while (i>0):
        s +=X[i-1]
        i -=1
    while (j>0):
        s +=Y[j-1]
        j -=1

    d=str(s[::-1])
    return d



 
 
X = "acbcf" 
Y = "abcdaf"
print ("print of shortest ", lcs(X, Y))