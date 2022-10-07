from collections import deque,defaultdict
#Adjacency list
def create_adj_list(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return adj

adj_list=create_adj_list([[0,1],[0,3],[1,2],[3,4],[3,7],[4,5],[4,6],[4,7],[5,6],[6,7]])

#Adjacency matrix

s=0
d=7
v=max(adj_list)+1
# v=len(adj_list)
vis=set()
parent=[0]*v
vis.add(s)
parent[s]=-1
q=deque([s])
while q:
    node=q.pop()
    for adjnode in range(v):
        if adjnode in adj_list[node] and adjnode not in vis:
            vis.add(adjnode)
            q.appendleft(adjnode)
            parent[adjnode]=node

ans=[]
curr=d
ans.append(d)
while curr!=s:
    curr=parent[curr]
    ans.append(curr)

print(ans[::-1])