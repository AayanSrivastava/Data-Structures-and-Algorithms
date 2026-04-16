#User function Template for python3
class Solution:
    def longestSubarrayDivK(self, arr, k):
        cursum = 0
        prefixsum = {0:-1}
        max_len = 0
        for i in range(len(arr)):
            cursum+=arr[i]
            remainder = cursum%k
            if remainder in prefixsum:
                max_len = max(max_len, i - prefixsum[remainder])
            else:
                prefixsum[remainder] = i
        
        return max_len