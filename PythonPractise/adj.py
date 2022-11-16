from collections import defaultdict
graph=[[1,2,3],[0,2,5],[0,1,3],[0,2]]
adj=defaultdict(list)
n=0
for i in range(len(graph)):
    adj[i].append(graph[i])
    n=max(n,max(graph[i]))
print(adj)