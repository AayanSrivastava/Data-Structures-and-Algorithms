from collections import defaultdict
class Solution:
    def dfs(self,node,vis,adj):
        vis.add(node)
        self.ans+=1
        for adjnode in adj[node]:
            if adjnode not in vis:
                self.dfs(adjnode,vis,adj)

    def countPairs(self, n, edges):
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        vis=set()
        output=[]
        for i in range(n):
            if i not in vis:
                self.ans=0
                self.dfs(i,vis,adj)
                output.append(self.ans)

        res=0
        for i in range(len(output)):
            res+=output[i]*(n-output[i])
        return res//2