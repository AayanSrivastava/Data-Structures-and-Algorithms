# Brute_force
class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        subarray = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i,len(nums)):
                if nums[j]%2!=0:
                    cnt+=1
                if cnt == k:
                    subarray+=1
                elif cnt > k:
                    break
        return subarray
'''
Convert each i to 1 (odd) or 0 (even) and accumulate.
Now the problem becomes: how many subarrays have sum exactly k in this 0/1 array.
'''
# prefix_sum
class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        prefixsum = {0: 1}
        cursum = 0
        cnt = 0
        for i in nums:
            cursum+=i%2
            cnt+=prefixsum.get(cursum-k,0)
            prefixsum[cursum]= prefixsum.get(cursum,0)+1
        
        return cnt