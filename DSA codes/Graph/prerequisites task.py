from collections import defaultdict,deque
class Solution:
    def isPossible(self,N,prerequisites):
        adj=defaultdict(list)
        indegree=[0]*N
        for src,dest in prerequisites:      #for i in prerequisites: adj[i[0]].append(i[1])
            adj[dest].append(src)
            indegree[src]+=1

        
        q=deque([])
        for i in range(N):
            if indegree[i]==0:
                q.append(i)
        ans=[] 
        while q:
            node=q.pop()
            ans.append(node)
            for adjnode in adj[node]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    q.append(adjnode)
        if len(ans)==N:
            return True
        return False
