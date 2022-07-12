from collections import deque
class Solution:
    def Bsearch(self,nums,t,start,end,first):
        if start>end:
            return first

        mid=start+(end-start)//2
        if nums[mid]==t:
            first=mid
            return self.Bsearch(nums,t,start,mid-1,first)
        if nums[mid]>t:
            return self.Bsearch(nums,t,start,mid-1,first)
        else:
            return self.Bsearch(nums,t,mid+1,end,first)
l=Solution()
ar=[3,3,3,4,5]
# ar=[7,6,5,4,3,2,1]  # reverse sorted array
first=-1
print(l.Bsearch(ar,3,0,len(ar)-1,first))