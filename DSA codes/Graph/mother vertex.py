from collections import defaultdict,deque
class Solution:
    
    #Function to find a Mother Vertex in the Graph.
    def dfs(self,node,adj,vis,ans):
        vis.add(node)
        ans.append(node)
        for adjnode in adj[node]:
            if adjnode not in vis:
                self.dfs(adjnode,adj,vis,ans)
                
    def findMotherVertex(self, V, adj):
        vis=set()
        for i in range(V):
            ans=[]
            if i not in vis:
                self.dfs(i,adj,vis,ans)
                if len(ans)==V:
                    return i
        return -1