import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n):
        heapq.heapify(arr)
        if n<2:
            return 0
        ans=0
        while len(arr)>1:
            s=0
            a=heapq.heappop(arr)
            b=heapq.heappop(arr)
            s+=a+b
            ans+=s
            arr.append(s)
        return ans