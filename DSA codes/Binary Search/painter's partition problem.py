class Solution:
    def isvalid(self,arr,n,k,mid):
        count=1
        sum=0
        for i in range(n):
            sum+=arr[i]
            if sum>mid:
                count+=1
                sum=arr[i]
                if count>k:
                    return False
        return True

    def minTime (self, arr, n, k):
        l=max(arr)
        h=sum(arr)
        res=-1
        while l<=h:
            mid=l+(h-l)//2
            if self.isvalid(arr,n,k,mid)==True:
                res=mid
                h=mid-1
            else:
                l=mid+1
        return res