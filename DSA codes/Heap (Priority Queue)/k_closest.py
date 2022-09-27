import heapq
def kclosest(ar,x,k):
    hp=[]
    for i in ar:
        if len(hp)<k:
            heapq.heappush(hp,(abs(i-x),i))
        else:
            if hp[0][0]>abs(i-x):
                heapq.heappush(hp,(abs(i-x),i))
                heapq.heappop(hp)
    hp=[hp[i][1] for i in range(k)]
    return hp

ar=[5,6,7,8,9]
x=7
k=3
print(kclosest(ar,x,k))