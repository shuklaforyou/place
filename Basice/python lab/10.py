n=int(input("enter "))
print("prime number are")
for num in range(0,n+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)  