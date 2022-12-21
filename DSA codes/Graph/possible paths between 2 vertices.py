from collections import deque
class Solution:
    def countPaths(self, V, adj, source, destination):
        ans=[]
        q=deque([(source,[source])])
        while q:
            node,path=q.popleft()
            if node==destination:
                ans.append(path)
            else:
                for adjnode in adj[node]:
                    q.append((adjnode, path + [adjnode]))
        return len(ans)