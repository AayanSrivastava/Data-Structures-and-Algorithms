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
            while(i>0 or j>0):
                if S[i-1]==S1[j-1]:
                    ans+=S[i-1]
                    i-=1
                    j-=1
                elif dp[i-1][j]>dp[i][j-1]:
                    ans+=S[i-1]
                    i-=1
                else:
                    ans+=S1[j-1]
                    j-=1
                
            while i>0:
                ans+=S[i-1]
                i-=1
            while j>0:
                ans+=S1[j-1]
                j-=1

            return ans[::-1]
    
    def plcs(self,S,S1):
        return self.printlcs(S,S1)
l1=Solution()
S="abac"
S1="cab"  #cabac
print("".join(l1.plcs(S,S1)))