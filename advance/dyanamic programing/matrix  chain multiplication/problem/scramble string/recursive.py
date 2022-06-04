def isScramble(S1: str, S2: str):
     
    # Strings of non-equal length
    # cant' be scramble strings
    if len(S1) != len(S2):
        return False
 
    n = len(S1)
 
    # Empty strings are scramble strings
    if not n:
        return True
 
    # Equal strings are scramble strings
    if S1 == S2:
        return True
 
    # Check for the condition of anagram
    if sorted(S1) != sorted(S2):
        return False
     
    # Checking if both Substrings are in
    # map or are already calculated or not
     
    # Declaring a flag variable
    flag = False
 
    for i in range(1, n):
         
        # Check if S2[0...i] is a scrambled
        # string of S1[0...i] and if S2[i+1...n]
        # is a scrambled string of S1[i+1...n]
        if (isScramble(S1[:i], S2[:i]) and
            isScramble(S1[i:], S2[i:])):
            flag = True
            return True
 
        # Check if S2[0...i] is a scrambled
        # string of S1[n-i...n] and S2[i+1...n]
        # is a scramble string of S1[0...n-i-1]
        if (isScramble(S1[-i:], S2[:i]) and
            isScramble(S1[:-i], S2[i:])):
            flag = True
            return True

     

    return False

S1 = "great"
S2 = "rgate"
     
if (isScramble(S1, S2)):
    print("Yes")
else:
    print("No")