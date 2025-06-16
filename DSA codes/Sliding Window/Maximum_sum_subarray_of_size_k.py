class Solution:
    def maximumSumSubarray (self,arr,k):
        i = 0
        window_sum = 0
        maxi = 0
        for j in range(len(arr)):
            window_sum+=arr[j]

            if j-i+1>k:
                window_sum-=arr[i]
                i+=1
            
            if j-i+1 == k:
                maxi = max(maxi, window_sum)
        return maxi
    
obj = Solution()
arr =  [100, 200, 300, 400] 
k = 2
print(obj.maximumSumSubarray(arr,k))