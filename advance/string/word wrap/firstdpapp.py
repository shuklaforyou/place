INF = 2147483647
def printSolution(p, n,M,l):
    count=0
    count1=0
    k = 0
    if p[n] == 1:
        k = 1
    else:
        k = printSolution(p, p[n] - 1,M,l) + 1
    for i in range(k-1):
        for t in range(p[n],n):
            if p[n]==n:
                count1=M-p[n]
                count= count + count1*count1
            else:
                for w in range(p[n],n):
                    cost = cost + l[w]+1
                    count1 = M-cost
                    count= count + count1*count1
    print(count)
    # print('Line number ', k, ': From word no. ',
    #                              p[n], 'to ', n)
    return k


def solveWordWrap (l, n, M):
    # For simplicity, 1 extra space is
    # used in all below arrays
 
    # extras[i][j] will have number
    # of extra spaces if words from i
    # to j are put in a single line
    extras = [[0 for i in range(n + 1)]
                 for i in range(n + 1)]
                  
    # lc[i][j] will have cost of a line
    # which has words from i to j
    lc = [[0 for i in range(n + 1)]
             for i in range(n + 1)]
              
    # c[i] will have total cost of
    # optimal arrangement of words
    # from 1 to i
    c = [0 for i in range(n + 1)]
     
    # p[] is used to print the solution.
    p = [0 for i in range(n + 1)]
     
    # calculate extra spaces in a single
    # line. The value extra[i][j] indicates
    # extra spaces if words from word number
    # i to j are placed in a single line
    for i in range(n + 1):
        extras[i][i] = M - l[i - 1]
        for j in range(i + 1, n + 1):
            extras[i][j] = (extras[i][j - 1] -
                                    l[j - 1] - 1)
                                     
    # Calculate line cost corresponding
    # to the above calculated extra
    # spaces. The value lc[i][j] indicates
    # cost of putting words from word number
    # i to j in a single line
    for i in range(n + 1):
        for j in range(i, n + 1):
            if extras[i][j] < 0:
                lc[i][j] = INF;
            elif j == n and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = (extras[i][j] *
                            extras[i][j])
 
    # Calculate minimum cost and find
    # minimum cost arrangement. The value
    # c[j] indicates optimized cost to
    # arrange words from word number 1 to j.
    c[0] = 0
    for j in range(1, n + 1):
        c[j] = INF
        for i in range(1, j + 1):
            if (c[i - 1] != INF and
                lc[i][j] != INF and
                ((c[i - 1] + lc[i][j]) < c[j])):
                c[j] = c[i-1] + lc[i][j]
                p[j] = i
    printSolution(p, n,M,l)
     
# Driver Code
l = [3, 2, 2, 5]
n = len(l)
M = 6
solveWordWrap(l, n, M)
