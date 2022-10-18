import heapq
def kclosest(arr,x,k):
    hp=[]
    for i in arr:
        if len(hp)<k:
            heapq.heappush(hp,(-abs(i-x),i))  #we need minimum so -abs
        else:
            if -hp[0][0]>abs(i-x):
                heapq.heappop(hp)
                heapq.heappush(hp,(-abs(i-x),i))
    return sorted([hp[i][1] for i in range(len(hp))])

arr=[5,6,7,8,9]
x=7
k=3
print(kclosest(arr,x,k))