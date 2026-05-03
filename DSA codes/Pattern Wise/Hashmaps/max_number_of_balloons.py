from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = Counter(text)
        have = Counter("balloon")
        res = float('inf')
        for i in "balloon":
            res = min(res,need[i]//have[i])
            
        return res if res!=float('inf') else 0


# 2nd approach -- avoid looping over balloon it has duplicates
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )