#notworking alerts please ||
def solve(s,i,j,isTrue):
    if (i > j) :
      return 0
    
    if (i == j) :
    
      if (isTrue == True) :
      
        return True if s[i] == 'T' else False
      
      else :
      
        return True if s[i] == 'F' else False

    temp_ans=0
    for k in range(i+1,j,2):

        lt=solve(s,i,k-1,True)
        lf=solve(s,i,k-1,False)
        rt=solve(s,k+1,j,True)
        rf=solve(s,k+1,j,False)

        
        if (s[k] == '&') :
            if (isTrue == True) :
                temp_ans = temp_ans + lt * rt
            else :
                temp_ans = temp_ans + lt * rf + lf * rt + lf * rf
        # Evaluate OR operation
        elif (s[k] == '|') :
            if (isTrue == True) :
                temp_ans = temp_ans + lt * rt + lt * rf + lf * rt
            else :
                temp_ans = temp_ans + lf * rf
    
      # Evaluate XOR operation
        elif (s[k] == '^') : 
            if (isTrue == True) :
                temp_ans = temp_ans + lt * rf + lf * rt
            else :
                temp_ans = temp_ans + lt * rt + lf * rf
            
    return temp_ans

a="T|F&T^F"
n=len(a)
i=0
j=n-1
print(solve(a,i,j,True))

