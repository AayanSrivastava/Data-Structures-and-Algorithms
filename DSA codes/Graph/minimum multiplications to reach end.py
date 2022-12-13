from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr, start, end): 
        q=deque([])
        dist=[10e9]*100000
        dist[start]=0
        q.append((start,0))
        mod=100000
        while q:
            node,steps=q.popleft()
            for i in arr:
                num=(i*node) % mod
                if steps+1<dist[num]:
                    dist[num]=steps+1
                    if num==end:
                        return steps+1
                    q.append((num,steps+1))
        return -1