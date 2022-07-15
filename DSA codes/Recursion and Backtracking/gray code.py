def solve(n):
    res=[]
    if n==1:
        res.append("0")
        res.append("1")
        return

    ans=[]
    r=solve(n-1)
    for i in range(len(r)):
        ans.append("0"+str(r[i]))
    for i in range(len(r)-1,-1,-1):
        ans.append("1"+str(r[i]))
    return ans

print(solve(3))