from collections import defaultdict,deque
n,m=map(int,input().split())
li=[]
for i in range(m):
    a,b=map(int,input().split())
    li.append([a,b])
print(li)
adj=defaultdict(list)
indegree=[0]*n
for src,dest in li:      #for i in prerequisites: adj[i[0]].append(i[1])
    adj[src].append(dest)
    indegree[src]+=1

print(adj)
q=deque([])
for i in range(n):
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
print(ans)