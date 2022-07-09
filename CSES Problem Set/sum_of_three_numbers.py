n,x=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
for i in range(len(nums)-2):
    l=i+1
    k=len(nums)-1
    while(l<k):
        tot=nums[i]+nums[l]+nums[k]
        if tot==x:
            a=i+1
            b=l+1
            c=k+1
            break
        elif tot<x:
            l=l+1
        elif tot>x:
            k=k-1
if a==0 and b==0 and c==0:
    print("IMPOSSIBLE")
else:
    print(a,b,c)