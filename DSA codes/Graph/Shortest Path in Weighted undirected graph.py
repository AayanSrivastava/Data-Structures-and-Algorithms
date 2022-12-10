from collections import defaultdict
class Solution:
    def shortestPath(self, n, m, edges):
        adj=defaultdict(list)
        for i,j,w in edges:
            adj[i].append((j,w))
            adj[j].append((i,w))
        
        parent=[0]*(n+1)
        for i in range(1,n+1):
            parent[i]=i
        s=set()
        dist=[10e9]*(n+1)
        dist[1]=0
        s.add((0,1))
        while s:
            dis,node=s.pop()
            for adjnode,edw in adj[node]:
                if dis+edw<dist[adjnode]:
                    dist[adjnode]=dis+edw
                    s.add((edw+dis,adjnode))
                    parent[adjnode]=node
        
        if dist[n]==10e9:
            return [-1]
        path=[]
        node=n
        while parent[node]!=node:
            path.append(node)
            node=parent[node]
        path.append(1)
        path.reverse()
        return path