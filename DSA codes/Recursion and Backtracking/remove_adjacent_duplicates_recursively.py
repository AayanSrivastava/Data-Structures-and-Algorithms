class Solution:
    def remove(self, S):
        if len(S) <= 1:
            return S

        if S[0] == S[1]:
            i = 1
            while i < len(S) and S[i] == S[0]:
                i += 1
            return self.remove(S[i:])
        else:
            rest = self.remove(S[1:])
            if rest and rest[0] == S[0]:
                return self.remove(rest)
            else:
                return S[0] + rest
        
if __name__ == "__main__":
    S = "geeksforgeek"
    obj = Solution()
    result = obj.remove(S)
    print(result)