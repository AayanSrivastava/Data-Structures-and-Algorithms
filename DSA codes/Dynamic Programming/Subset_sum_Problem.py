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
    
    #TABULATION
    def subsetTab(self,arr,target):
        dp=[[0]*(target+1) for i in range(len(arr)+1)]
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
        for i in range(len(arr)+1):
            cur=[0]*(target+1)
            for j in range(target+1):
                if i==0 and j==0:
                    cur[j]=True
                elif i==0:
                    cur[j]=0
                elif j==0:
                    cur[i]=1
                else:
                    nottake=prev[j]
                    if target>=arr[i-1]:
                        take=prev[j-arr[i-1]]
                    cur[j]=take or nottake
            prev=cur
        return prev[target]
        
    def isSubsetSum (self, N, arr, sum):
        # dp=[[-1]*(sum+1) for i in range(N+1)]
        # return self.subset(arr,0,sum,dp)
        # return self.subsetTab(arr,sum)
        return self.subsetOpt(arr,sum)