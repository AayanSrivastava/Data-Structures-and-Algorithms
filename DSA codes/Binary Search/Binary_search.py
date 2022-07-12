class Solution:
    def Bsearch(self,nums,t,start,end):
        if start>end:
            return -1

        mid=start+(end-start)//2
        if nums[mid]==t:
            return mid
        if nums[mid]>t:
            return self.Bsearch(nums,t,start,mid-1)
        else:
            return self.Bsearch(nums,t,mid+1,end)

l=Solution()
ar=[1,3,2,3,4,5,3,7]
# ar=[7,6,5,4,3,2,1]  # reverse sorted array
print(l.Bsearch(ar,3,0,len(ar)-1))