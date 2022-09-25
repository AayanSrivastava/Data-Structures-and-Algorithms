# def getKthLargest(arr, k):
#     op=[]
#     for i in range(len(arr)):
#         sum1=0
#         for j in range(i,len(arr)):
#             sum1+=arr[j]
#             op.append(sum1)
#     op.sort()
#     return op[-k]

import heapq
class Solution:
    def kthLargest(self, N : int, K : int, Arr ):
        op=[]
        for i in range(N):
            sum1=0
            for j in range(i,N):
                sum1+=Arr[j]
                op.append(sum1)
        hp=[]
        heapq.heapify(hp)
        for i in op:
            if len(hp)<K:
                heapq.heappush(hp,i)
            else:
                if hp[0]<i:
                    heapq.heappush(hp,i)
                    heapq.heappop(hp)
    
        return hp[0]