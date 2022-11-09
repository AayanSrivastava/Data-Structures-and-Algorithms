a=[2,8,5,4]
def findpos(a):
    d={}
    for pos,el in enumerate(a):
        d[pos]=el
    return d

c=0
prev=findpos(a)
print(prev)
a.sort()
cur=findpos(a)
print(cur)
for i in range(len(a)):
    if prev[i]!=cur[i]:
        prev[]
        f=prev.index(cur[i][0])
        prev[i][0],f[0]=f[0],prev[i][1]
        c+=1
print(prev)
print(c)