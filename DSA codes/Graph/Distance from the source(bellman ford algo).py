class Solution:
    def bellman_ford(self, V, edges, S):
        dist=[100000000]*V
        dist[S]=0
        for i in range(V-1):
            for i,j,w in edges:
                if(dist[i]!=1e8 and dist[i]+w<dist[j]):
                    dist[j]=dist[i]+w
        
        for i,j,w in edges:
            if(dist[i]!=1e8 and dist[i]+w<dist[j]):
                return [-1]
                
        return dist