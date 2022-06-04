# tet=4
# pte=7
# ans=tet^pte
# print(ans)

# n= int(input())
# for i in range(1,n+1):
#     print(i,end="")



string="11101010101010"
inputstring=str(string)
n=len(inputstring)
sub="10"
sub1="11"
for i in range(n):
    if sub in inputstring:
        inputstring=inputstring.replace("10","",1)
        
    elif sub1 in inputstring :
        inputstring=inputstring.replace("11","",1)
            
print(len(inputstring))
    
        

# string="11101010101010"
# string=str(string)
# inputstring=[]
# for i in range(len(string)):
#     inputstring.append(string[i])
# n=len(inputstring)-1
# print(n)
# print(inputstring)
# sub="1"
# sub2="0"
# sub1="1"
# count=0
# i=0
# while i<n:
#     test=inputstring[i]
#     test1=inputstring[i+1]
#     if test=='1' and test1=='1':
#         count= count+2
#         i +=2
        
     
#     if test=='1' and test1=='0':
#         count =count + 2
#         i+=2
     
#     else:
#         i+=1
            
# print(count)
# print(len(inputstring)-count-2)
    
        

        

        

