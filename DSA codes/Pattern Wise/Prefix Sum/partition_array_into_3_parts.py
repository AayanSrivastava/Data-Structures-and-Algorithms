'''
total//3 will not solve all the problem , it will just tell if its possible or not
but it wont tell if that sum is contiguous or random.
'''


class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        total = sum(arr)
        
        if total % 3 != 0:
            return False
        
        target = total // 3
        curr = 0
        count = 0
        
        for num in arr:
            curr += num
            if curr == target:
                count += 1
                curr = 0
        
        return count >= 3