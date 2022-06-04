from collections import defaultdict
def printDups(st):
    count=defaultdict(int)
    for i in range(len(st)):
        count[st[i]] +=1

    for it in count :
        if count:
            print(it,",count=",count[it])

if __name__=="__main__":
    st="test string"
    printDups(st)


#working code