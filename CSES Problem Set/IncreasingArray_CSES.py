n=int(input())
nums=list(map(int,input().split()))
s=0
for i in range(1,len(nums)):
    while(nums[i]<=nums[i-1]):
        s+=1
        nums[i]+=1
print(s)