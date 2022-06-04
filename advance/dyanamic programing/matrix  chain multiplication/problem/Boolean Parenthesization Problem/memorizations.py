
def pc(Str, i, j, isTrue, t) :
    
    if (i > j) :
      return 0
    
    if (i == j) :
    
      if (isTrue == 1) :
      
        return 1 if Str[i] == 'T' else 0
      
      else :
      
        return 1 if Str[i] == 'F' else 0
    
    if (t[i][j][isTrue] != -1) :
      return t[i][j][isTrue]
    
    temp_ans = 0
    
    for k in range(i + 1, j, 2) :
    
      if (t[i][k - 1][1] != -1) :
        LT = t[i][k - 1][1]
      else :
        # Count number of True in left Partition
        LT = pc(Str, i, k - 1, 1, t)
        
      if (t[i][k - 1][0] != -1) :
        LF = t[i][k - 1][0]
      else :
        # Count number of False in left Partition
        LF = pc(Str, i, k - 1, 0, t)
     
      if (t[k + 1][j][1] != -1) :
        RT = t[k + 1][j][1]
      else :
        # Count number of True in right Partition
        RT = pc(Str, k + 1, j, 1, t)
      
      if (t[k + 1][j][0] != -1) :
        RF = t[k + 1][j][0]
      else :
        # Count number of False in right Partition
        RF = pc(Str, k + 1, j, 0, t)
    
      # Evaluate AND operation
      if (Str[k] == '&') :
        if (isTrue == 1) :
          temp_ans = temp_ans + LT * RT
        else :
          temp_ans = temp_ans + LT * RF + LF * RT + LF * RF
      # Evaluate OR operation
      elif (Str[k] == '|') :
        if (isTrue == 1) :
          temp_ans = temp_ans + LT * RT + LT * RF + LF * RT
        else :
          temp_ans = temp_ans + LF * RF
    
      # Evaluate XOR operation
      elif (Str[k] == '^') : 
        if (isTrue == 1) :
          temp_ans = temp_ans + LT * RF + LF * RT
        else :
          temp_ans = temp_ans + LT * RT + LF * RF
      t[i][j][isTrue] = temp_ans

    return temp_ans
    
def countWays(N, S) :
 
    t = [[[-1 for k in range(2)] for i in range(N + 1)] for j in range(N + 1)] 
    return pc(S, 0, N - 1, 1, t)
 
symbols = "T|T&F^T"
# operators = "|&^"
S = "T|T&F^T"
# j = 0
# for i in range(len(symbols)) :

#   S = S + symbols[i]
#   if (j < len(operators)) :
#     S = S + operators[j]
#     j += 1

# We obtain the string  T|T&F^T
N = len(S)

# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and
# (T|((T&F)^T))
print(countWays(N, S))