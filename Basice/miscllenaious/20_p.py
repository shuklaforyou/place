def gcd(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and  y%i==0:
            gcd1=i

    return gcd1

num1=54
num2=24
print(gcd(num1,num2))
