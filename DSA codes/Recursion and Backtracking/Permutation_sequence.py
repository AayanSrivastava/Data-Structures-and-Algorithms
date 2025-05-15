class Solution:
    def solve(self, S, ans, index):
        if index == len(S):
            ans.append(''.join(S[:]))
            return
        
        for i in range(index, len(S)):
            S[index], S[i] = S[i], S[index]
            self.solve(S, ans, index+1)
            S[index], S[i] = S[i], S[index]

    
    def kth_permutation(self, n, k):
        S=[]
        for i in range(1, n+1):
            S.append(str(i))
        ans=[]
        self.solve(S, ans, 0)
        ans.sort()
        return ans[k-1]

if __name__ == "__main__":
    obj = Solution()
    n = 3
    k = 3
    print(obj.kth_permutation(n, k))
