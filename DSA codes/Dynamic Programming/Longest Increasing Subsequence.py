import bisect
class Solution:
    def solve(self,arr,n,cur,prev,dp):
        if cur==n:
            return 0
        
        if dp[cur][prev+1]!=-1:
            return dp[cur][prev+1]

        take=0
        if prev==-1 or arr[cur]>arr[prev]:
            take=1+self.solve(arr,n,cur+1,cur,dp)
        
        nottake=0+self.solve(arr,n,cur+1,prev,dp)
        dp[cur][prev+1]=max(take,nottake)
        return dp[cur][prev+1]
        
    def solvetab(self,arr,n):
        dp=[[0]*(n+1) for i in range(n+1)]
        for cur in range(n-1,-1,-1):
            for prev in range(cur-1,-2,-1):
                take=0
                if prev==-1 or arr[cur]>arr[prev]:
                    take=1+dp[cur+1][cur+1]
                
                nottake=0+dp[cur+1][prev+1]
                dp[cur][prev+1]=max(take,nottake)
        return dp[0][0]
    
    def solveopt(self,arr,n):
        nextdp=[0]*(n+1)
        for cur in range(n-1,-1,-1):
            curdp=[0]*(n+1)
            for prev in range(cur-1,-2,-1):
                take=0
                if prev==-1 or arr[cur]>arr[prev]:
                    take=1+nextdp[cur+1]
                
                nottake=0+nextdp[prev+1]
                curdp[prev+1]=max(take,nottake)
            nextdp=curdp
        return nextdp[0]
    
    def solveBinarySearch(self,arr,n):
        temp=[arr[0]]
        for i in range(1,n):
            if arr[i]>temp[-1]:
                temp.append(arr[i])
            else:
                ind=bisect.bisect_left(temp,arr[i])
                temp[ind]=arr[i]
        return len(temp)
        
    def lengthOfLIS(self, nums):
        n=len(nums)
        # dp=[[-1]*(n+1) for i in range(n)]
        # return self.solve(nums,n,0,-1,dp)
        # return self.solvetab(nums,n)
        # return self.solveopt(nums,n)
        return self.solveBinarySearch(nums,n)