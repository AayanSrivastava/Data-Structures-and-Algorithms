from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        cnt = 0
        mini = float('inf')
        i = 0
        res = ""
        for j in range(len(s)):
            if count[s[j]]>0:
                cnt+=1
            count[s[j]]-=1

            while cnt == len(t):
                if j-i+1 < mini:
                    mini = j-i+1
                    res = s[i:j+1]
            
                count[s[i]]+=1
                if count[s[i]]>0:
                    cnt-=1
                i+=1
            
        return res