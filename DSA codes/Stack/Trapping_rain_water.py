a=[3,0,0,2,0,4]
maxl=[]
maxr=[0]*(len(a)-1)
water=[]

maxl.append(a[0])
maxr.append(a[-1])

# print(maxl)
# print(maxr)

for i in range(1,len(a)):
    maxl.append(max(maxl[i-1],a[i]))

for i in range(len(a)-2,-1,-1):
    maxr[i]=max(maxr[i+1],a[i])


# print(maxr)
# print(maxl)

for i in range(len(a)):
    water.append(min(maxl[i],maxr[i])-a[i])

print(sum(water))