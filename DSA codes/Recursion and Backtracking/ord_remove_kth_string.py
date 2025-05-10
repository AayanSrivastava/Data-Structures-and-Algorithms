class Solution:
    def kthcharacter(self, k):
        s = ["a"]
        while len(s)<k:
            string = []
            for i in s:
                string.append((chr( (ord(i)- ord('a')+1)  % 26 + ord('a'))))
            s.extend(string)
        # print(s)
        return s[k-1]


    #Using recursion
    def kth_sol(self,s,k):
        if len(s)>=k:
            return s[k-1]
        for i in s:
            s+=chr((ord(i)-ord('a') + 1 ) % 26 + ord('a'))
        return self.kth_sol(s,k)
    def kthCharacterrec(self, k: int) -> str:
        s="a"
        return self.kth_sol(s,k)


if __name__ == "__main__":
    obj = Solution()
    print(obj.kthcharacter(3))