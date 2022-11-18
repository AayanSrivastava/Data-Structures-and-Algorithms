from collections import deque,defaultdict
class Solution:
    def countPaths(self, n, roads):
        adj=defaultdict(list)
        for city1,city2,time in roads:
            # adj[city1].append(city2)
            # adj[city2].append(city1)

            adj[city1].append((city2,time))
            adj[city2].append((city1,time))
        
        destination = n-1
        ans=[]
        q=deque([(0,[0])])
        while q:
            node,path=q.popleft()
            if node==destination:
                ans.append(path)
            else:
                for adjnode in adj[node]:
                    q.append((adjnode, path + [adjnode]))
        return adj

l=Solution()    
n=7
roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(l.countPaths(n,roads))