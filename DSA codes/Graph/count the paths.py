#DFS
from collections import defaultdict
class Solution:
    def possible_paths(self, edges, n, s, d):
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
        ans=[]
        stack=[(s,[0])]
        while stack:
            node,path=stack.pop()
            if node==d:
                ans.append(path)
            else:
                for adjnode in adj[node]:
                    stack.append((adjnode,path+[adjnode]))
        return len(ans)
        # return ans