from collections import deque

def create_adj(edges):
    no_of_nodes=1+ max([e[0] for e in edges] + [e[1] for e in edges])
    adj=[[0]*no_of_nodes for i in range(no_of_nodes)]
    for e in edges:
        adj[e[0]][e[1]]=1   #directed graph
        adj[e[1]][e[0]]=1
    return adj

adj_mat_undir=create_adj([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])

def bfs(adj):
    print("BFS")
    vis=set()
    n=len(adj)
    for i in range(n):
        if i in vis:
            continue
        vis.add(i)

        q=deque([i])
        while q:
            node=q.pop()
            print(node,end=" ")
            
            for adjnode in range(n):
                if adj[node][adjnode] and adjnode not in vis:
                    vis.add(adjnode)
                    q.appendleft(adjnode)
    print()

bfs(adj_mat_undir)