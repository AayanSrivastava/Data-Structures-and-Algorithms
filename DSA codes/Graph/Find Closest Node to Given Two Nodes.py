from collections import defaultdict
class Solution:
    def dis(self,node,adj,edges,dist):
        vis=set()
        q=[node]
        while q:
            node1=q.pop()
            distance=dist[node1]
            vis.add(node1)
            for adjnode in adj[node1]:
                if adjnode not in vis:
                    dist[adjnode]=distance+1
                    q.append(adjnode)
                    vis.add(adjnode)
        return dist

    def closestMeetingNode(self, edges, node1, node2):
        adj=defaultdict(list)
        for i in range(len(edges)):
            if edges[i]!=-1:
                adj[i].append(edges[i])
        
        dist=[float('inf') for i in range(len(edges))]
        dist[node1]=0
        self.dis(node1,adj,edges,dist)
        dist1=dist
        dist=[float('inf') for i in range(len(edges))]
        dist[node2]=0
        self.dis(node2,adj,edges,dist)
        res=float('inf')
        ans=-1
        # return dist1,dist
        for i, (a, b) in enumerate(zip(dist1, dist)):
            if max(a, b) < res:
                res = max(a, b)
                ans=i
        return ans