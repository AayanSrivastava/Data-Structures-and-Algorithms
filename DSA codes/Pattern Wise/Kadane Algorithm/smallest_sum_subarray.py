class Solution:
    def smallestSumSubarray(self, A, N):
        bestending = res = A[0]
        for i in range(1, len(A)):
            v1 = bestending + A[i]
            v2 = A[i]
            
            bestending = min(v1, v2)
            res = min(res, bestending)
        
        return res