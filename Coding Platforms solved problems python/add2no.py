t=123
t=str(t)
t=list(t)
for i in range(len(t)):
    t[i]=int(t[i])
print(list(t))