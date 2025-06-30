class Solution:
    def longestUniqueSubstr(self, s):
        left = 0
        maxi = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxi = max(maxi, right-left+1)
        return maxi