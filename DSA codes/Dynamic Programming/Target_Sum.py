class Solution:
    def ways(self,arr,target):
        n=len(arr)
        dp=[[0]*(target+1) for i in range(len(arr)+1)]
        dp[0][0]=1
            
        for j in range(1,target+1):
            dp[0][j]=0
            
        for i in range(1,len(arr)+1):
            for t in range(target+1):
                nottake=dp[i-1][t]
                take=0
                if t>=arr[i-1]:
                    take=dp[i-1][t-arr[i-1]]
                dp[i][t]= (take + nottake)
        
        return dp[n][target]
    
    # def subset(self,arr,ind,target,dp):
    #     if ind==0:
    #         if target==0 and arr[0]==0:
    #             return 2
    #         if target==0 or arr[0]==target:
    #             return 1
    #         return 0
        
    #     if dp[ind][target]!=-1:
    #         return dp[ind][target]
            
    #     nottake=self.subset(arr,ind-1,target,dp)
    #     take=0
    #     if target>=arr[ind]:
    #         take=self.subset(arr,ind-1,target-arr[ind],dp)
    #     dp[ind][target]= (take+nottake)
    #     return dp[ind][target]
    
    # def ways(self,arr,tar):
    #     n=len(arr)
    #     dp=[[-1]*(tar+1) for i in range(len(arr))]
    #     return self.subset(arr,n-1,tar,dp)
        
    def countPartitions(self, n, d, arr):
        totsum=sum(arr)
        if totsum-d<0 or (totsum-d)%2!=0:
            return 0
        return self.ways(arr,(totsum-d)//2)

    def findTargetSumWays(self, arr, N, target):
        return self.countPartitions(N,target,arr)