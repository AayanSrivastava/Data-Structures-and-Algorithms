from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        maxi, max_count = 0,0
        for i in range(len(s)):
            count = defaultdict(int)
            for j in range(i, len(s)):
                count[s[j]]+=1
                max_count = max(max_count, count[s[j]])
                if (j-i+1) - max_count > k:
                    count[s[j]]-=1
                    break
                else:
                    maxi = max(maxi, j-i+1)
        return maxi
    
#OPTIMISED
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi, max_count = 0,0
        count = defaultdict(int)
        i = 0
        for j in range(len(s)):
            count[s[j]]+=1
            max_count = max(max_count, count[s[j]])

            if (j-i+1) - max_count > k:
                count[s[i]]-=1
                i+=1
            
            maxi = max(maxi, j-i+1)
        return maxi