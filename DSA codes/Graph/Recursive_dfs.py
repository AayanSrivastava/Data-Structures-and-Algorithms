from collections import deque,defaultdict

#Adjacency list
def create_adj_list(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return adj

adj_list=create_adj_list([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])
# adj_list=create_adj_list([[0,1],[0,2],[0,3],[1,3],[2,4],[3,5],[3,6],[4,7]])

#Adjacency matrix
def create_adj_mat(edges):
    no_of_nodes=1+ max([e[0] for e in edges] + [e[1] for e in edges])
    adj=[[0]*no_of_nodes for i in range(no_of_nodes)]
    for e in edges:
        adj[e[0]][e[1]]=1   #directed graph
        adj[e[1]][e[0]]=1
    return adj

adj_mat=create_adj_mat([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])
# adj_mat=create_adj_mat([[0,1],[0,2],[0,3],[1,3],[2,4],[3,5],[3,6],[4,7]])


def dfs(node,vis,adj,ans):
    vis.add(node)
    ans.append(node)
    # n=len(adj)
    n=max(adj)+1
    for adjnode in range(n):
        # if adj[node][adjnode] and adjnode not in vis:
        if adjnode in adj[node] and adjnode not in vis:  #Adjacency list
            dfs(adjnode,vis,adj,ans)


def dfsofGraph(adj):
    ans=[]
    vis=set()
    n=max(adj)+1
    # n=len(adj)
    for i in range(n):
        if i not in vis:
            dfs(i,vis,adj,ans)
    return ans

# print(dfsofGraph(adj_mat))
print(dfsofGraph(adj_list))