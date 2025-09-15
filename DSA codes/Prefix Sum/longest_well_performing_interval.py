class Solution:
    def longestWPI(self, hours) -> int:
        cursum = 0
        prefixsum = {}
        maxi = 0
        for i in range(len(hours)):
            if hours[i]>8:
                cursum+=1
            else:
                cursum-=1

            if cursum > 0:
                maxi = i + 1
            else:
                if cursum-1 in prefixsum:
                    maxi = max(maxi, i - prefixsum[cursum-1])
            if cursum not in prefixsum:
                prefixsum[cursum] = i
        return maxi