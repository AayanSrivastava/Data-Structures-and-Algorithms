from typing import List

class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        prefix_max = [0] * N
        suffix_min = [0] * N
        
        # Build prefix max
        prefix_max[0] = A[0]
        for i in range(1, N):
            prefix_max[i] = max(prefix_max[i-1], A[i])
        
        # Build suffix min
        suffix_min[N-1] = A[N-1]
        for i in range(N-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], A[i])
        
        # Count valid cuts
        count = 0
        for i in range(N-1):
            if prefix_max[i] + suffix_min[i+1] >= K:
                count += 1
        
        return count
