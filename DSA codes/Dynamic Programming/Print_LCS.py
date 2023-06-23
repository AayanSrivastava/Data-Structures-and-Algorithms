class Solution:
    def printlcs(self,S,S1):
            n,m=len(S),len(S1)
            dp=[[0]*(m+1) for i in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if S[i-1]==S1[j-1]:
                        dp[i][j] = 1+ dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
            ans=""
            i,j=n,m
            while(i>0 and j>0):
                if S[i-1]==S1[j-1]:
                    ans+=S[i-1]
                    i-=1
                    j-=1
                elif dp[i-1][j]>dp[i][j-1]:
                    i-=1
                else:
                    j-=1
            return ans
    def plcs(self,S,S1):
        return self.printlcs(S,S1)
l1=Solution()
S="abgca"
S1="abeca"
print("".join(l1.plcs(S,S1)))