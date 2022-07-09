def Bsearch(nums,t,start,end):
    first=-1
    if start>end:
        return -1

    else:
        mid=start+(end-start)//2
        if nums[mid]==t:
            first=mid
            end=mid-1
            return Bsearch(nums,t,start,end)
        if nums[mid]>t:
            return Bsearch(nums,t,start,mid-1)
        else:
            return Bsearch(nums,t,mid+1,end)
    return first

ar=[1,3,2,3,4,5,3,7]
# ar=[7,6,5,4,3,2,1]  # reverse sorted array
print(Bsearch(ar,3,0,len(ar)-1))