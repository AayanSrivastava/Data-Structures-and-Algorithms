from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        flag = True
        res = 0
        for i in cnt:
            if cnt[i]%2 == 0:
                res+=cnt[i]
            else:
                res+=cnt[i]-1
                if flag:
                    res+=1
                    flag = False
            
        return res