class Solution:
    def LISTracePrint(self,arr,n):
        dp=[1]*n
        hashh=[0]*n
        maxi=1
        arr.sort()
        lastindex=0
        for i in range(n):
            hashh[i]=i
            for prev in range(i):
                if arr[i]%arr[prev]==0 and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    hashh[i]=prev
            if dp[i]>maxi:
                maxi=dp[i]
                lastindex=i
        
        temp=[]
        temp.append(arr[lastindex])
        while hashh[lastindex]!=lastindex:
            lastindex=hashh[lastindex]
            temp.append(arr[lastindex])
        return temp[::-1]
        
    def LargestSubset(self, n, arr):
        return self.LISTracePrint(arr,n)