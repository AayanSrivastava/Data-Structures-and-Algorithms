from collections import Counter
class Solution:
    def search(self,pat, txt):
        i = 0
        cnt = 0
        k = len(pat)
        pat_count = Counter(pat)
        window_count = Counter()
        for j in range(len(txt)):
            window_count[txt[j]]+=1
            
            if j - i + 1 > k:
                window_count[txt[i]]-=1
                if window_count[txt[i]]==0:
                    del window_count[txt[i]]
                i+=1
                
            if j - i + 1 == k:
                if pat_count == window_count:
                    cnt+=1
        return cnt