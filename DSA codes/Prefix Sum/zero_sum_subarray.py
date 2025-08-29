class Solution:
    def findSubarray(self, arr):
        cnt = 0
        cursum = 0
        prefixsum = {0 : 1}
        for i in arr:
            cursum+=i
            cnt+=prefixsum.get(cursum, 0)
            prefixsum[cursum] = prefixsum.get(cursum, 0)+1
        return cnt
