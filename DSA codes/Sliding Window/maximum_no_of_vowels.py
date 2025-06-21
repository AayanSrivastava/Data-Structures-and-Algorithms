#remove the character only when s[i] is a vowel only
# TC - O(n), SC - O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        vowels = set('aeiou')
        maxi = 0
        count = 0
        for j in range(len(s)):
            if s[j] in "aeiou":
                count+=1

            if j-i+1>k:
                if s[i] in "aeiou":
                    count-=1
                i+=1

            if j-i+1 == k:
                maxi = max(maxi,count)
            
        return maxi
    
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        window=""
        maxi = 0
        for j in range(len(s)):
            if s[j] in "aeiou":
                window+=s[j]

            if j-i+1>k:
                if s[i] in "aeiou":
                    window=window[:-1]
                i+=1

            if j-i+1 == k:
                maxi = max(maxi,len(window))
            
        return maxi