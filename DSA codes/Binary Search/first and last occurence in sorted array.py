class Solution:
    def Bsearchf(self,nums,t,start,end,first):
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]==t:
                first=mid
                return self.Bsearchf(nums,t,start,mid-1,first)
            if nums[mid]>t:
                return self.Bsearchf(nums,t,start,mid-1,first)
            else:
                return self.Bsearchf(nums,t,mid+1,end,first)
        return first
            
l=Solution()
ar=[3,3,3,4,5]
# ar=[7,6,5,4,3,2,1]  # reverse sorted array
first=-1
print(l.Bsearchf(ar,3,0,len(ar)-1,first))