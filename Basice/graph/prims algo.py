

import sys
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        key=[sys.maxsize for i in range(V)]
        mst=[False for i in range(V)]
        parent=[0 for i in range(V)]
        pq=[]
        heapq.heappush(pq,(0,0))
        key[0]=0
        parent[0]=-1
        while len(pq)!=0:
            u=heapq.heappop(pq)[1]
            mst[u]=True
            for it in adj[u]:
                v=it[0]
                weight=it[1]
                if mst[v]==False and weight<key[v]:
                    parent[v]=u
                    key[v]=weight
                    heapq.heappush(pq,(key[v],v))
                    
        sum=0
        for i in range(V):
            sum+=key[i]
        return sum
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))