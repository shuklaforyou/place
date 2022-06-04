no_of_chars=256
def fillcharcount(string,count):
    for i in string:
        count[ord(i)]+=1
        return count 

def printdups(string):
    count=[0]*no_of_chars
    count=fillcharcount(string,count)
    
    print(count)
    for i in count:
        if int(i)>1:
            print(count[i]+",count="+str(i))
            

string="test string"
print(printdups(string))


#not working code