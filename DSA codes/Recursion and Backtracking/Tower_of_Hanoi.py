def TOH(n,source,destination,helper,c):
    if n==0:
        return
    TOH(n-1,source,helper,destination,c)
    print("Move disk",n,"from rod",source,"to rod",destination)
    c+=1
    TOH(n-1,helper,destination,source,c)
    print(c)

c=0
TOH(3,1,2,3,c)