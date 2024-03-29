class Solution:

    #MEMOIZATION
    def subset(self,arr,ind,target,dp):
        if ind==len(arr):
            if target==0:
                return True
            return False
        
        if dp[ind][target]!=-1:
            return dp[ind][target]
            
        nottake=self.subset(arr,ind+1,target,dp)
        take=False
        if target>=arr[ind]:
            take=self.subset(arr,ind+1,target-arr[ind],dp)
        dp[ind][target]= take or nottake
        return dp[ind][target]
    
    #from N-1
    def subset(self,arr,ind,target,dp):
        if target==0:
            return True
        if ind==len(arr):
            return 0
        
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
        
    def isSubsetSum (self, N, arr, sum):
        # dp=[[-1]*(sum+1) for i in range(N+1)]
        # return self.subset(arr,0,sum,dp)
        # return self.subset(arr,N-1,sum,dp)
        # return self.subsetTab(arr,sum)
        return self.subsetOpt(arr,sum)