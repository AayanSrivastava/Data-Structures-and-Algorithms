#DFS
class Solution:
    def topo(self,node,vis,adj,st):
        vis.add(node)
        for adjnode in adj[node]:
            if adjnode not in vis:
                self.topo(adjnode,vis,adj,st)
        
        st.append(node)
        
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        vis=set()
        st=[]
        for i in range(V):
            if i not in vis:
                self.topo(i,vis,adj,st)
        
        ans=[]
        while st:
            ans.append(st.pop())
        return ans