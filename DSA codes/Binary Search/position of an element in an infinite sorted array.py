class Solution:
    def Bsearch(self,nums,l,h,x):
        first=-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==x:
                return mid
            if nums[mid]<x:
                return self.Bsearch(nums,mid+1,h,x)
            return self.Bsearch(nums,l,mid-1,x)
        return first

    def position(self,nums,x):
        l=0
        h=1
        while x>nums[h]:
            l=h
            h=h*2
        return self.Bsearch(nums,l,h,x)

l=Solution()
nums=[1,2,5,4,5,6,7,8,9,11,22,33,44,55,66,77,88]
print(l.position(nums,5))