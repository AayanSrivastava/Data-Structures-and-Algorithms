from collections import defaultdict
class Solution:
    def dfs(self,node,vis,adj,st):
        vis.add(node)
        for adjnode in adj[node]:
            if adjnode[0] not in vis:
                self.dfs(adjnode[0],vis,adj,st)
        
        st.append(node)
        
    def shortestPath(self, n,m,edges):
        adj=defaultdict(list)
        for i,j,wt in edges:
            adj[i].append((j,wt))
        
        vis=set()
        st=[]
        for i in range(n):
            if i not in vis:
                self.dfs(i,vis,adj,st)
            
        dist=[float('inf')]*n
        dist[0]=0
        while st:
            node=st.pop()
            for adjnode in adj[node]:
                v=adjnode[0]
                wt=adjnode[1]
                
                if dist[node]+wt<dist[v]:
                    dist[v]=dist[node]+wt
                    
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist