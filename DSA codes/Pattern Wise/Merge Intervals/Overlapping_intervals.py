class Solution:
    def isIntersect(self, intervals):
        intervals.sort()
        merged = []
        cnt = 0
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
                continue
            else:
                cnt+=1
            
        return cnt>0