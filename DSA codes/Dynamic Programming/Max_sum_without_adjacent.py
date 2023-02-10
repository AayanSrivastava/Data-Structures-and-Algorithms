class Solution:
	def maxsum(self,arr,n,dp):
		if n==0:
			return arr[n]
		if n<0:
			return 0
		if n==1:
			return max(arr[0],arr[1])
		if dp[n]!=-1:
			return dp[n]
		pick=arr[n]+self.maxsum(arr,n-2,dp)
		notpick=0+self.maxsum(arr,n-1,dp)
		
		dp[n]=max(pick,notpick)
		return dp[n]
		
	def maxsumTab(self,arr,n):
		dp=[-1]*(n+1)
		dp[0]=arr[0]
		if n>=1:
			dp[1]=max(arr[0],arr[1])
		for i in range(2,n+1):
			dp[i]=max((dp[i-2]+arr[i]),(dp[i-1]))
		return dp[n]
	
	#SPACE OPTIMIZATION
	def maxspaceOpt(self,arr,n):
		prev2=0
		prev=arr[0]
		for i in range(1,n):
			cur=max(arr[i]+prev2,prev)
			prev2=prev
			prev=cur
		return prev

	def findMaxSum(self,arr, n):
	   # dp=[-1]*(n+1)
	   # return self.maxsum(arr,n-1,dp)
	   
	#    return self.maxsumTab(arr,n-1)
	   
	   return self.maxsumOpt(arr,n)