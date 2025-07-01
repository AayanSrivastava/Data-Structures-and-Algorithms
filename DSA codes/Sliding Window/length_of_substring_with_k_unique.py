def longestKSubstr(self, s, k):
        maxi = -1
        for i in range(len(s)):
            seen = set()
            sub = ""
            for j in range(i, len(s)):
                sub+=s[j]
                seen.add(s[j])
                if len(seen)<k:
                    continue
                if len(seen)==k:
                    maxi = max(maxi, j-i+1)
                else:
                    break
        return maxi

#OPTIMISED
# ============
from collections import defaultdict
class Solution:

    def longestKSubstr(self, s, k):
        maxi = -1
        i = 0
        dic = defaultdict(int)
        for j in range(len(s)):
            dic[s[j]]+=1
                
            while len(dic)>k:
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
                i+=1
                
            if len(dic)==k:
                maxi = max(maxi, j-i+1)
                
        return maxi