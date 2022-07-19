class Solution:
    def Bsearchf(self,nums,t,start,end,last):
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]==t:
                last=mid
                return self.Bsearchf(nums,t,mid+1,end,last)
            if nums[mid]>t:
                return self.Bsearchf(nums,t,start,mid-1,last)
            else:
                return self.Bsearchf(nums,t,mid+1,end,last)
        return last
            
l=Solution()
ar=[1,2,3,3]
# ar=[7,6,5,4,3,2,1]  # reverse sorted array
last=-1
print(l.Bsearchf(ar,3,0,len(ar)-1,last))