from collections import defaultdict
class Solution:
    def topo(self,node,vis,adj,st):
        vis.add(node)
        for adjnode in adj[node]:
            if adjnode not in vis:
                self.topo(adjnode,vis,adj,st)
        st.append(node)
        
    def dfs(self,node,vis,adjr):
        vis.add(node)
        for adjnode in adjr[node]:
            if adjnode not in vis:
                self.dfs(adjnode,vis,adjr)
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        st=[]
        vis=set()
        for i in range(V):
            if i not in vis:
                self.topo(i,vis,adj,st)
            
        # step 2 - reverse the graph
        vis=set()
        adjr=defaultdict(list)
        for i in range(V):
            for adjnode in adj[i]:
                adjr[adjnode].append(i)
            
        # step 3 - dfs
        scc=0
        while st:
            node=st.pop()
            if node not in vis:
                scc+=1
                self.dfs(node,vis,adjr)
        return scc


# Kosaraju's algo for printing components
from collections import defaultdict
class Solution:
    def topo(self,node,vis,adj,st):
        vis.add(node)
        for adjnode in adj[node]:
            if adjnode not in vis:
                self.topo(adjnode,vis,adj,st)
        st.append(node)
        
    def dfs(self,node,vis,adjr,component):
        vis.add(node)
        component.append(node)
        for adjnode in adjr[node]:
            if adjnode not in vis:
                self.dfs(adjnode,vis,adjr,component)
    
    #Function to find number of strongly connected components in the graph
    def tarjans(self, V, adj):
        st=[]
        vis=set()
        for i in range(V):
            if i not in vis:
                self.topo(i,vis,adj,st)
            
        # step 2 - reverse the graph
        vis=set()
        adjr=defaultdict(list)
        for i in range(V):
            for adjnode in adj[i]:
                adjr[adjnode].append(i)
            
        # step 3 - dfs
        ans=[]
        while st:
            node=st.pop()
            component=[]
            if node not in vis:
                self.dfs(node,vis,adjr,component)
            if component:
                ans.append(sorted(component))
        return sorted(ans)