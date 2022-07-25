class Solution:
    def isvalid(self,A,N,M,mx):
        students=1
        sum=0
        for i in range(N):
            sum+=A[i]
            if sum>mx:
                students+=1
                sum=A[i]
            if students>M:
                return False
        return True
        
    def findPages(self,A, N, M):
        if N<M:
            return -1
        start=max(A)
        end=sum(A)
        res=-1
        while start<=end:
            mid=start+(end-start)//2
            if self.isvalid(A,N,M,mid)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res

l=Solution()
ar=[10,20,30,40]
n=4
m=2
print(l.findPages(ar,n,m))