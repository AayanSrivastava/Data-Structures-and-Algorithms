from collections import defaultdict,deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        dist=[float('inf')]*n
        dist[src]=0
        q=deque([src])
        while q:
            node=q.pop()
            for adjnode in adj[node]:
                if dist[node]+1<dist[adjnode]:
                    dist[adjnode]=dist[node]+1
                    q.append(adjnode)
                
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist