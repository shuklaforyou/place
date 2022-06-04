def isplindrom(n):
    return str(n)[::-1]==str(n)
def rev(n): #reverse functiob work in string
    return str(n)[::-1]

n=input()
while(1):
    n= int(n)+int(rev(n))
    if (isplindrom(n)):
        print(n)
        break   


# working code

