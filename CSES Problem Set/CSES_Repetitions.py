n=input()
max=1
c=1
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c+=1
        if c>max:
            max=c
    else:
        c=1
print(max)