class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        
        # Step 1: Transform array
        transformed = [1 if x > k else -1 for x in arr]
        
        prefix = 0
        max_len = 0
        first_occurrence = {}
        
        for i in range(n):
            prefix += transformed[i]
            
            # Case 1: whole subarray is valid
            if prefix > 0:
                max_len = i + 1
            
            # Store first occurrence
            if prefix not in first_occurrence:
                first_occurrence[prefix] = i
            
            # Case 2: check if prefix-1 exists
            if (prefix - 1) in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix - 1])
        
        return max_len