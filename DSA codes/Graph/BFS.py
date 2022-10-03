from collections import deque,defaultdict

#Adjacency list
def create_adj_list_dir(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return adj

# adj_list_dir=create_adj_list_dir([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])
adj_list_dir=create_adj_list_dir([[0,4]])
print(adj_list_dir)
for i in adj_list_dir:
    print(adj_list_dir[i])
# print(max(adj_list_dir))

#Adjacency matrix
def create_adj(edges):
    no_of_nodes=1+ max([e[0] for e in edges] + [e[1] for e in edges])
    adj=[[0]*no_of_nodes for i in range(no_of_nodes)]
    for e in edges:
        adj[e[0]][e[1]]=1   #directed graph
        adj[e[1]][e[0]]=1
    return adj

adj_mat_undir=create_adj([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])
# print(adj_mat_undir)
# print(len(adj_mat_undir))

def bfs(adj):
    print("BFS")
    vis=set()
    # n=len(adj)  #Adjacency matrix
    n=max(adj)+1 #Adjacency list
    for i in range(n):
        if i in vis:
            continue
        vis.add(i)

        q=deque([i])
        while q:
            node=q.pop()
            print(node,end=" ")
            
            for adjnode in range(n):
                if adjnode in adj[node] and adjnode not in vis:
                    vis.add(adjnode)
                    q.appendleft(adjnode)

            # for adjnode in adj[node]:
            #         if adjnode not in vis:
            #             vis.add(adjnode)
            #             q.appendleft(adjnode)
        
        # if returning list return here(indentation)
    print()

# bfs(adj_mat_undir)
# bfs(adj_list_dir)