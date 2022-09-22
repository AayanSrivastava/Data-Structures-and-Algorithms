import heapq
class heap:
    def insert(self,arr,val):
        heapq.heappush(arr,val)
    
    def delete(self,arr):
        heapq.heappop(arr)

l=heap()
arr=[]
l.insert(arr,5)
l.insert(arr,6)
l.insert(arr,3)
l.insert(arr,8)
l.insert(arr,7)
# heapq.heapify(arr)
print(arr)
l.delete(arr)
print(arr)