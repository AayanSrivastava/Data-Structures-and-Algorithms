def TOH(n,source,destination,helper,c):
    if n==0:
        return
    TOH(n-1,source,helper,destination,c)
    print("Move disk",n,"from rod",source,"to rod",destination)
    c+=1
    TOH(n-1,helper,destination,source,c)
    print(c)

s=1
h=2
d=3
n=2
c=0
print(TOH(2,s,d,h,c))