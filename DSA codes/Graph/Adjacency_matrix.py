def create_adj(edges):
    no_of_nodes=1+ max([e[0] for e in edges] + [e[1] for e in edges])
    adj=[[0]*no_of_nodes for i in range(no_of_nodes)]
    for e in edges:
        adj[e[0]][e[1]]=1   #directed graph
        adj[e[1]][e[0]]=1
    return adj

adj_mat=create_adj([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])
for x in adj_mat:
    print(x)


# Method-2

# def create_adj(n,m):
#     adj=[[0]*(n+1) for i in range(m+1)]
#     for i in range(m):
#         u,v=map(int,input().split())
#         adj[u][v]=1
#     return adj

# adj_mat=create_adj(4,4)
# for x in adj_mat:
#     print(x)