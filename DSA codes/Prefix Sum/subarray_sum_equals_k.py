#Brute force
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            subsum=0
            for j in range(i,n):
                subsum+=nums[j]
                if subsum == k:
                    cnt+=1
        return cnt


# prefix sum
# cursum = 0
# cnt = 0
# prefixsum = {0 : 1}
# for i in nums:
#     cursum+=i
#     cnt+=prefixsum.get(cursum-k,0)
#     prefixsum[cursum] = prefixsum.get(cursum,0) + 1

# return cnt
l = Solution()
nums=[1,1,1]
k = 2
print(l.subarraySum(nums,k))