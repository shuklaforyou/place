def find_permutation( s,answer):
        
            # Code here
    if len(s)==0:
        print(answer,end=" ")
        return
            
    for i in range(len(s)):
        ch=s[i]
        left_subtr =s[0:i]
        right_subtr = s[i+1:]
        rest = left_subtr + right_subtr
        find_permutation(rest,answer + ch)
    
answer = ""
s = input()
find_permutation(s,answer)