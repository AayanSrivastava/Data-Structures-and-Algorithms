def toh(n,a,b,c,ans):
    if n==0:
        return
    toh(n-1,a,c,b,ans)
    ans.append((a,c))
    toh(n-1,b,a,c,ans)
        
def towerOfHanoi(n):
    ans=[]
    if n==0:
        return ans
    toh(n,1,2,3,ans)
    return ans

print(towerOfHanoi(4))