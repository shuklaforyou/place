def findSingle(ar ,n):
    res = ar[0]

    for i in range(1,n):
        res = res^ar[i]
    return res

ar=[2,3,5,4,5,3,4]
print("Element occurring once is ", findSingle(ar,len(ar)))


#Q1. Find the only non-repeating element in an array where every other element
#repeats twice. - 
