class Solution:
    def reverse_exponentiation(self, n):
        p = 1
        if n == 10:
            p = 1
        else:
            p = n
        return self.power(n, p)
    
    def power(self, n, p):
        if p == 1:
            return n
        ans = self.power(n, p//2)
        if p % 2 == 0:
            return ans * ans
        else:
            return n * ans * ans
    
if __name__ == "__main__":
    n = 3
    l = Solution()
    print(l.reverse_exponentiation(n))