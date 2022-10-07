#BFS
from collections import defaultdict, deque
def toposort(v,adj):
    indegree=[0]*v
    for i in range(v):
        for adjnode in adj[i]:
            indegree[adjnode]+=1
    q=deque([])
    for i in range(v):
        if indegree[i]==0:
            q.append(i)
        
    ans=[]
    while q:
        node=q.popleft()
        ans.append(node)
        for adjnode in adj[node]:
            indegree[adjnode]-=1
            if indegree[adjnode]==0:
                q.append(adjnode)
    return ans

#Adjacency list
def create_adj_list(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        # adj[e[1]].append(e[0])
    return adj

adj_list=create_adj_list([[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]])

print(toposort(max(adj_list)+1,adj_list))