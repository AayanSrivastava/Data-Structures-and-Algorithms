from collections import defaultdict
edges =  [[1,2],[2,3]]
adj=defaultdict(list)
for i,j in edges:
    adj[i].append(j)

print(adj)
n=max([i[0] for i in edges]+ [i[1] for i in edges])
print(n)
for i in range(1,n+1):
    if len(adj[i])==0 and i not in adj[i]: 
        print(i)