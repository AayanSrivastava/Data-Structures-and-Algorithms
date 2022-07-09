# import queue
# a=[5,6,3,9,5,7,3,4,8]
# q=queue.PriorityQueue()
# for i in a:
#     q.put(i)
# print(q.poll())
import heapq
nums=[1,5,4,5]
heapq.heapify(nums)
print(nums)
for i in range(len(nums)):
    nums[i]*=-1

heapq.heapify(nums)
print(nums)
x=-heapq.heappop(nums)-1
y=-heapq.heappop(nums)-1

print(x*y)