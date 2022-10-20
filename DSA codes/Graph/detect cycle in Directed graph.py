from collections import deque
class Solution:
    def isCyclic(self, V, adj):
        indegree=[0]*V
        for i in range(V):
            for adjnode in adj[i]:
                indegree[adjnode]+=1
        q=deque([])
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        cnt=0 
        while q:
            node=q.pop()
            cnt+=1
            for adjnode in adj[node]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    q.append(adjnode)
        return cnt!=V