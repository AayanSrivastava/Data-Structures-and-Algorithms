from collections import defaultdict,deque
rooms = [[1,3],[3,0,1],[2],[0]]
adj=defaultdict(list)
for i,room in enumerate(rooms):
    adj[i]=room

q=deque([0])
node=q.popleft()
for i in adj[node]:
    print(i)