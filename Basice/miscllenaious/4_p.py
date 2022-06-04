t={}

k = int(input().split()[1])

l = [int(i) for i in input().split()]

for i in l:
     print(i,k ,'t')

     try: t[i%k] += 1

  
     except: t[i%k] = 1
     
    
   

print(sum(t[i] * (t[i]-1) for i in t))
