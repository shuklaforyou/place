class solutions:
    def rec_perm(self,S,N,used,stack,res):
        if len(stack)==N:
            res.append("".join(stack))
            return
        for i in range(N):
            if used[i]!=1:
                stack.append(S[i])
                used[i]=1
                self.rec_perm(S,N,used,stack,res)
                stack.pop()
                used[i]=0

    def find_permutation(self,S):
        res=[]
        stack=[]
        N=len(S)
        used=[0]*N
        self.rec_perm(S,N,used,stack,res)
        return sorted(res)


ob=solutions()
S="BC"
print(ob.find_permutation(S))