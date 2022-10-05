from collections import deque,defaultdict
class Solution:
    def isbfscycle(self,i,vis,adj):
        vis.add(i)
        q=deque([[i,-1]])
        n=len(adj)
        while q:
            node,parent=q.pop()
            for adjnode in range(n):
                if adj[node][adjnode]:
            # for adjnode in adj[node]:   #Adjacency List
                    if adjnode not in vis:
                        vis.add(adjnode)
                        q.appendleft([adjnode,node])
                    elif adjnode!=parent:
                        return True
        return False
	    
    def isCycle(self,V,adj):
        vis=set()
        for i in range(V):
            if i not in vis:
                if self.isbfscycle(i,vis,adj):
                    return True
        return False

    #Adjacency List
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

l=Solution()
# print(l.isCycle(len(l.adj_list),l.adj_list))
print(l.isCycle(len(l.adj_mat),l.adj_mat))