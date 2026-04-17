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
    
# when returning index
    def findSplit(self, arr):
        n = len(arr)
        total = sum(arr)
        if total%3!=0:
            return [-1,-1]
        
        target = total//3
        cur = 0
        i = -1
        j = -1
        for idx in range(n):
            cur+=arr[idx]
            
            if cur == target and i == -1:
                i = idx
            elif cur == 2*target and i!=-1:
                j = idx
                break
        if i != -1 and j != -1 and j < len(arr) - 1:
            return [i, j]
    
        return [-1, -1]