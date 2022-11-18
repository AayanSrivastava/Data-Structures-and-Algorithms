from collections import deque,defaultdict
class Solution:    
    def eventualSafeNodes(self, V,adj):
        adjrev=defaultdict(list)
        indegree=[0]*V
        for i in range(V):
            for adjnode in adj[i]:
                adjrev[adjnode].append(i)
        
        for i in range(V):
            for adjnode in adjrev[i]:
                indegree[adjnode]+=1
            
        q=deque([])
        for i in range(V):
            if indegree[i]==0:
                q.append(i)

        safenodes=[]
        while q:
            node=q.popleft()
            safenodes.append(node)
            for adjnode in adjrev[node]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    q.append(adjnode)
        
        safenodes.sort()
        return safenodes