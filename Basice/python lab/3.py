def power(base,exp):
    if exp==1:
        return base
    if exp!=1:
        return base*power(base,exp-1)

base=int(input("Enter:-"))
exp=int(input("enter:-"))
print(power(base,exp))