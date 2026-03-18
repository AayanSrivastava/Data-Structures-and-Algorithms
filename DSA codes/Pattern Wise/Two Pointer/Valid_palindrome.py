class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        new_s = [i.lower() for i in s if i.isalnum()]
        
        i = 0
        j = len(new_s)-1
        while i<j:
            if new_s[i]!=new_s[j]:
                return False
            i+=1
            j-=1
        return True