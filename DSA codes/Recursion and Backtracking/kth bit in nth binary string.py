class Solution:
    def solve(self,n):
        s1=""
        s=""
        ans=""

        if n==1:
            return "0"
        
        s=self.solve(n-1)
        for i in range(len(s)):
            if s[i]=='0':
                s1+='1'
            else:
                s1+='0'

        ans = s + '1' + s1[::-1]
        return ans

    def findKthBit(self, n,k):
        st=self.solve(n)
        return st[k-1]

l=Solution()
n=4
k=11
print(l.findKthBit(n,k))