from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = Counter(ransomNote)
        have = Counter(magazine)
        for i in need:
            if have[i] < need[i]:
                return False
            
        return True