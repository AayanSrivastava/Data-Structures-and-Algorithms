class Solution:
	def  minDifference(self, arr, n):
	# TABULATION
		totsum=sum(arr)
		k=totsum
		dp=[[False]*(k+1) for i in range(n)]
		for i in range(n):
			dp[i][0]=True
		if k>=arr[0]:
			dp[0][arr[0]]=True
		
		for ind in range(1,n):
			for target in range(1,k+1):
				nottake=dp[ind-1][target]
				take=False
				if target>=arr[ind]:
					take=dp[ind-1][target-arr[ind]]
				dp[ind][target]=take or nottake
		
		mini=1e9
		for s1 in range(totsum//2+1):
			if dp[n-1][s1]==True:
				mini=min(mini,abs(s1-(totsum-s1)))
		
		return mini
	
	#Space_Optimization

	# totsum=sum(arr)
	# k=totsum
	# prev=[0]*(k+1)
	# prev[0]=True
	# prev[arr[0]]=True
	# for ind in range(1,n):
	#     cur=[0]*(k+1)
	#     cur[0]=True
	#     for target in range(1,k+1):
	#         nottake=prev[target]
	#         take=False
	#         if k>=arr[ind]:
	#             take=prev[target-arr[ind]]
	#         cur[target]=take or nottake
	#     prev=cur
		
	# mini=1e9
	# for s1 in range(totsum//2+1):
	#     if prev[s1]==True:
	#         mini=min(mini,abs(s1-(totsum-s1)))
		
	# return mini