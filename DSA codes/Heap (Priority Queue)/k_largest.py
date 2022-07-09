from heapq import heappop,heapify
k=2
nums=[3,2,1,5,6,4]
heapify(nums)
while len(nums)>k:
    heappop(nums)
    print(nums)