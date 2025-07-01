from collections import defaultdict
class Solution:
    def countSubstring(self, s):
        cnt = 0
        for i in range(len(s)):
            dic = defaultdict(int)
            for j in range(i,len(s)):
                dic[s[j]]=1
                if dic['a']+dic['b']+dic['c'] == 3:
                    cnt+=1
        return cnt
    

#OPTIMISED

from collections import defaultdict
class Solution:
    def countSubstring(self, s):
        i = 0
        cnt = 0
        dic = defaultdict(int)
        for j in range(len(s)):
            dic[s[j]]+=1

            while dic['a'] > 0 and dic['b'] > 0 and dic['c'] > 0:
                cnt+=len(s)-j
                dic[s[i]]-=1
                i+=1
            
        return cnt