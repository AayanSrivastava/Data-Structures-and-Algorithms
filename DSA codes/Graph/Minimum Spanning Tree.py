import heapq
class Solution:
    def spanningTree(self, V, adj):
        minheap=[[0,0]]
        vis=set()
        sum1=0
        while minheap:
            wt,node=heapq.heappop(minheap)
            if node in vis:
                continue
            vis.add(node)
            sum1+=wt
            for adjnode,edw in adj[node]:
                if adjnode not in vis:
                    heapq.heappush(minheap,[edw,adjnode])
        return sum1