from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        cnt = 0
        mapper = defaultdict(int)
        for j in range(len(s)):
            mapper[s[j]]+=1

            while j-i+1 > 3:
                mapper[s[i]]-=1
                if mapper[s[i]]==0:
                    del mapper[s[i]]
                i+=1
            
            if len(mapper) == 3 and j - i + 1 == 3:
                cnt+=1
        return cnt