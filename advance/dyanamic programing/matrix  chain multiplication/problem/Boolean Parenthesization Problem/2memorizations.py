def pc(Str, i, j, isTrue) :
    
    if (i > j) :
      return 0
    
    if (i == j) :
    
      if (isTrue == 1) :
      
        return 1 if Str[i] == 'T' else 0
      
      else :
      
        return 1 if Str[i] == 'F' else 0

    temp_ans = 0
    
    for k in range(i + 1, j, 2) :
        LT = pc(Str, i, k - 1, 1)
        LF = pc(Str, i, k - 1, 0)
        RT = pc(Str, k + 1, j, 1)
        RF = pc(Str, k + 1, j, 0)
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

    return temp_ans

def countWays(N, S):
    return pc(S, 0, N - 1, 1)

S = "T|T&F^T"
N = len(S)
print(countWays(N, S))
    