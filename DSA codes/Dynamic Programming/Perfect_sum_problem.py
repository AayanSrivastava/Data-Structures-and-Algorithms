class Solution:
    def subset(self,arr,ind,target,dp):
        if ind==len(arr):
            if target==0:
                return 1
            return 0
        
        if dp[ind][target]!=-1:
            return dp[ind][target]%1000000007
         
        nottake=0  
        nottake=self.subset(arr,ind+1,target,dp)%1000000007
        take=0
        if target>=arr[ind]:
            take=self.subset(arr,ind+1,target-arr[ind],dp)%1000000007
        dp[ind][target]= (take+nottake)%1000000007
        return dp[ind][target]
        
    def perfectSum(self, arr, n, sum):
        dp=[[-1]*(sum+1) for i in range(n+1)]
        return self.subset(arr,0,sum,dp)%1000000007