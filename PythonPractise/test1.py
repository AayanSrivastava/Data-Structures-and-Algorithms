# from collections import defaultdict,Counter
# edges =  [[1,2],[2,3]]
# adj=defaultdict(list)
# for i,j in edges:
#     adj[i].append(j)

# a=[]
# print(adj)
# for i in adj:
#     a.extend(adj[i])
# print(a)

# print(adj)
# n=max([i[0] for i in edges]+ [i[1] for i in edges])
# print(n)
# for i in range(1,n+1):
#     if len(adj[i])==0 and i not in adj[i]: 
#         print(i)


a=[4,6,3,8,2]
print(set(a))
print(a.pop())