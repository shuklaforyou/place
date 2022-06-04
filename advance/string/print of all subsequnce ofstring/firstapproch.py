def printSub(input,output):
    #Method 1 (Pick and Don’t Pick Concept)  
    if len(input)==0:
        print(output,end=' ')
        return 
    printSub(input[1:],output+input[0])
    printSub(input[1:],output)

input="abc"
output=""
print(printSub("abc",""))  