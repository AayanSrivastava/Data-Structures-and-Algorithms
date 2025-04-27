def isvalid(A,N,k,mx):
    index=A[0]
    sum=1
    for i in range(N):
        if A[i]-index >= mx:
            sum+=1
            if sum==k:
                return True
            index=A[i]
    return False

def aggressiveCows(stalls, k):
    stalls.sort()
    N=len(stalls)
    start=0
    end=max(stalls)
    res=-1
    while start<=end:
        mid=start+(end-start)//2
        if isvalid(stalls,N,k,mid)==True:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res