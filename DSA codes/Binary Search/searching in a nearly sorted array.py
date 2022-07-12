def nearlysorted(nums,l,h,k):
    while l<=h:
        mid=l+(h-l)//2
        if nums[mid]==k:
            return mid
        elif mid-1>=l and nums[mid-1]==k:
            return mid-1
        elif mid+1<=h and nums[mid+1]==k:
            return mid+1
        
        elif nums[mid]<k:
            l=mid+2
        elif nums[mid]>k:
            h=mid-2
    return -1

nums=[3, 2, 10, 4, 40]
print(nearlysorted(nums,0,len(nums)-1,4))