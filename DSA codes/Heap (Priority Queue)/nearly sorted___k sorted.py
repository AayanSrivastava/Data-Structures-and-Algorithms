import heapq
class Solution:
    def nearlySorted(self,a,n,k):
        ans=[]
        heapq.heapify(a)
        while len(a)>0:
            ans.append(heapq.heappop(a))
        return ans

# METHOD-II

# class Solution:
#     def nearlySorted(self,a,n,k):
#         hp=[]
#         ans=[]
#         for i in a:
#             if len(hp)<k:
#                 heapq.heappush(hp,i)
#             else:
#                 heapq.heappush(hp,i)
#                 ans.append(heapq.heappop(hp))
#         while len(hp)>0:
#             ans.append(heapq.heappop(hp))
#         return ans
