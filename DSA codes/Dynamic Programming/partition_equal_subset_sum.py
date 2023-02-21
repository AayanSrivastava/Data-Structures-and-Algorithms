class Solution:
    #MEMOIZATION
    def subset(self,arr,ind,target,dp):
        if target==0:
            return True
        if ind==len(arr):
            return False
        
        if dp[ind][target]!=-1:
            return dp[ind][target]
            
        nottake=self.subset(arr,ind+1,target,dp)
        take=False
        if target>=arr[ind]:
            take=self.subset(arr,ind+1,target-arr[ind],dp)
        dp[ind][target]= take or nottake
        return dp[ind][target]
    
    #TABULATION
    def subsetTab(self,arr,target):
        dp=[[0]*(target+1) for i in range(len(arr)+1)]
        for i in range(len(arr)):
            dp[i][0]=True
        if target>=arr[0]:
            dp[0][arr[0]]=True
        for i in range(1,len(arr)):
            for t in range(1,target+1):
                nottake=dp[i-1][t]
                take=False
                if target>=arr[i]:
                    take=dp[i-1][t-arr[i]]
                dp[i][t]=take or nottake
        return dp[len(arr)-1][target]

    #SPACE_OPTIMIZATION
    def subsetOpt(self,arr,target):
        prev=[0]*(target+1)
        prev[0]=True
        if target>=arr[0]:
            prev[arr[0]]=True
        for i in range(1,len(arr)):
            cur=[0]*(target+1)
            for j in range(1,target+1):
                nottake=prev[j]
                take=False
                if target>=arr[i]:
                    take=prev[j-arr[i]]
                cur[j]=take or nottake
            prev=cur
        return prev[target]

    def canPartition(self, nums):
        totsum=0
        for i in nums:
            totsum+=i
        if totsum%2!=0:
            return False
        target=totsum//2
        dp=[[-1]*(target+1) for i in range(len(nums)+1)]
        return self.subset(nums,0,target,dp)
        # return self.subset(nums,target)