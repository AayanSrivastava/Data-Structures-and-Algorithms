class Solution:
    def numOfSubarrays(self, arr, k, threshold) -> int:
        i = 0
        cnt = 0
        window_sum = 0
        for j in range(len(arr)):
            window_sum+=arr[j]

            while j-i+1 > k:
                window_sum-=arr[i]
                i+=1
            
            if j-i+1 == k and window_sum//(j-i+1) >=threshold:
                cnt+=1
            
        return cnt