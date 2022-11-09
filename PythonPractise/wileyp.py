s='yyyaaaann'
h={}
for i in s:
    if i in h:
        h[i]+=1
    else:
        h[i]=1
print(sorted(h.items(),key=lambda kv:(kv[1],kv[0]),reverse=True))