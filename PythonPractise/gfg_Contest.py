a=[4,3,2,1]
N=4
arpos=[*enumerate(a)]
arpos.sort(key=lambda x:x[1])
print(arpos)
vis=[0]*N
ans=0
for i in range(N):
    if vis[i] or arpos[i][0]==i:
        continue
    steps=0
    j=i
    while not vis[j]:
        vis[j]=1
        j=arpos[j][0]
        steps+=1
    if steps>0:
        ans+=steps-1
print(ans)
