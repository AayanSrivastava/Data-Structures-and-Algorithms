S="abbb"
h={}
for i in S:
    if i in h:
        h[i]+=1
    else:
        h[i]=1

res = [S[i: j] for i in range(len(S)) for j in range(i + 1, len(S) + 1)]
for i in res:
    pass
print(set(res))