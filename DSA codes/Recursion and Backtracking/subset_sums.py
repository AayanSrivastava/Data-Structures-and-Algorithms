class Solution:
    def solve(self, index, sum1, arr, ans):
        if index==len(arr):
            ans.append(sum1)
            return
        
        #include
        self.solve(index+1, sum1+arr[index], arr, ans)
        #exclude
        self.solve(index+1, sum1, arr, ans)

    def subsetSum(self, arr):
        ans=[]
        self.solve(0, 0, arr, ans)
        return ans
    
if __name__ == "__main__":
    obj = Solution()
    arr= [2,3]
    ans = obj.subsetSum(arr)
    ans.sort()
    print(ans)
    

