class Solution:
    def solve(self,arr,n):
        dp=[1]*n
        cnt=[1]*n
        maxi=1
        for i in range(n):
            for prev in range(i):
                if arr[prev]<arr[i] and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    cnt[i]=cnt[prev]
                elif arr[prev]<arr[i] and 1+dp[prev]==dp[i]:
                    cnt[i]+=cnt[prev]
            maxi=max(maxi,dp[i])
        
        nos=0
        for i in range(n):
            if dp[i]==maxi:
                nos+=cnt[i]
        return nos
        
    def NumberofLIS(self, n, arr):
        return self.solve(arr,n)