class Solution:
    def Bsearchf(self,nums,t,start,end,first):
        if start>end:
            return first

        mid=start+(end-start)//2
        if nums[mid]==t:
            first=mid
            return self.Bsearchf(nums,t,start,mid-1,first)
        if nums[mid]>t:
            return self.Bsearchf(nums,t,start,mid-1,first)
        else:
            return self.Bsearchf(nums,t,mid+1,end,first)

    def Bsearchl(self,nums,t,start,end,last):
        if start>end:
            return last

        mid=start+(end-start)//2
        if nums[mid]==t:
            last=mid
            return self.Bsearchl(nums,t,mid+1,end,last)
        if nums[mid]>t:
            return self.Bsearchl(nums,t,start,mid-1,last)
        else:
            return self.Bsearchl(nums,t,mid+1,end,last)
l=Solution()
ar=[1,3,3,4,5]
# ar=[7,6,5,4,3,2,1]  # reverse sorted array
first=-1
last=-1
print(l.Bsearchf(ar,3,0,len(ar)-1,first))
print(l.Bsearchl(ar,3,0,len(ar)-1,last))