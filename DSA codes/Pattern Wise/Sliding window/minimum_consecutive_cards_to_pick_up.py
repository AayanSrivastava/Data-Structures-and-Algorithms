from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards) -> int:
        i = 0
        mini = float('inf')
        mapper = defaultdict(int)
        for j in range(len(cards)):
            mapper[cards[j]]+=1
            
            while mapper[cards[j]]>1:
                mini = min(mini,j-i+1)
                mapper[cards[i]]-=1
                i+=1

        return mini if mini!=float('inf') else -1