def countRev(s):
    temp, res, n = 0, 0, len(s)
 
    if (n % 2 != 0):
        return -1
    for i in range(n):
        if (s[i] == '{'):
            temp += 1
        else:
            if (temp == 0):
                res += 1
                temp += 1
            else:
                temp -= 1
 
    if (temp > 0):
        res += temp // 2
    return res

s="}}{{"
print(countRev(s))