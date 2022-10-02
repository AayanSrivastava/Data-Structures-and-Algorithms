from collections import defaultdict

# Directed
def create_adj_list_dir(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
    return adj

adj_list_dir=create_adj_list_dir([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])

def create_adj_list(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return adj

adj_list=create_adj_list([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])
print(adj_list)