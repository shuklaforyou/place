int= 32
def lrotate(n,d):
    return (n << d)|(n >> ( int-d))
def rrotate(n,d):
    return (n >> d)|(n << (int-d)) & 0xFFFFFFFF

n=16
d=2

print("left rotate of ",n,"by"
      ,d,"is" , end="")
print(lrotate(n,d))

print("rigt rotate of n ",n,"by"
      ,d,"is" ,end="")
print(rrotate(n,d))
