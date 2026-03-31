from collections import defaultdict
class Solution:
    def countGood(self, nums, k: int) -> int:
        i = 0
        cnt = 0
        freq = defaultdict(int)
        pairs = 0
        n = len(nums)
        for j in range(n):
            pairs+=freq[nums[j]]
            freq[nums[j]]+=1

            while pairs>=k:
                cnt+=n-j
                freq[nums[i]]-=1
                pairs-=freq[nums[i]]
                i+=1
            
        return cnt