from collections import deque,defaultdict


#Adjacency list
def create_adj_list(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return adj

adj_list=create_adj_list([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])

#Adjacency matrix
def create_adj_mat(edges):
    no_of_nodes=1+ max([e[0] for e in edges] + [e[1] for e in edges])
    adj=[[0]*no_of_nodes for i in range(no_of_nodes)]
    for e in edges:
        adj[e[0]][e[1]]=1   #directed graph
        adj[e[1]][e[0]]=1
    return adj

adj_mat=create_adj_mat([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])

def dfs(adj):
    print("DFS")
    vis=set()
    # n=len(adj)
    n=max(adj)+1
    for i in range(n):
        if i in vis:
            continue
        vis.add(i)

        q=deque([i])
        while q:
            node=q.pop()
            print(node,end=" ")
            
            for adjnode in range(n):
                # if adj[node][adjnode] and adjnode not in vis: #Adjacency Matrix
                if adjnode in adj[node] and adjnode not in vis: #Adjacency Lisr
                    vis.add(adjnode)
                    q.append(adjnode)
    print()

# dfs(adj_mat)
dfs(adj_list)
