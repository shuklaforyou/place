def ispowerfour(n):
    if ( n==0 ):
        return False

    while (n !=1):
        if (n%4!=0):
            return False
        n=n//4

    return True

n=64
if (ispowerfour(n)):
    print(n,'is a power of 4')
else:
    print(n,'is not a power of 4')
