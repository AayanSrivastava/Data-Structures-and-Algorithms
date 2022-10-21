def dijkstra(self, V, adj, S):
    s=set()
    ans=[10e9]*V
    s.add((0,S))
    ans[S]=0
    while s:
        dist,prev=s.pop()
        for ele,w in adj[prev]:
            w_new=w+dist
            if w_new<ans[ele]:
                s.add((w_new,ele))
                ans[ele]=w_new
    return ans