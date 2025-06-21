from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        i = 0
        ans = []
        k = len(p)
        pat_count = Counter(p)
        window_count = Counter()
        for j in range(len(s)):
            window_count[s[j]]+=1

            if j - i + 1 > k:
                window_count[s[i]]-=1
                if window_count[s[i]]==0:
                    del window_count[s[i]]
                i+=1

            if j - i + 1 == k:
                if pat_count == window_count:
                    ans.append(i)
        return ans