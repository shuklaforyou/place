class Solution:
    def findtoposort(self,node,vis,stack,adj):
        vis[node]=1
        for it in adj[node]:
            if vis[it]==0:
                self.findtoposort(it,vis,stack,adj)
                
        stack.append(node)
        
    #Function to return list containing vertices in Topological order.
    def topoSort(self, n, adj):
        # Code here
        vis=[0 for _ in range(n)]
        stack=[]
        for i in range(n):
            if vis[i]==0:
                self.findtoposort(i,vis,stack,adj)
                    
        
        topo=[]
        while  stack:
            topo.append(stack.pop())
            
        return print(topo)
        
    




import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
