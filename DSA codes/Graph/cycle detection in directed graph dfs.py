from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def dfs(self,node,vis,adj,pathvis):
        vis.add(node)
        pathvis.add(node)
        for adjnode in adj[node]:
            if adjnode not in vis:
                if self.dfs(adjnode,vis,adj,pathvis):
                    return True
            elif adjnode in pathvis:
                return True
        
        pathvis.remove(node)
        return False
        
    def isCyclic(self, V, adj):
        vis=set()
        pathvis=set()
        for i in range(V):
            if i not in vis:
                if self.dfs(i,vis,adj,pathvis):
                    return True
        return False