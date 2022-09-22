def solve(s):
    buff,x,cv=s[0], 1, 1
    for i in range(1,len(s)):
        if buff==s[i]: 
            cv+=1
        else:
            x*=cv
            cv,buff = 1,s[i]
    return x*cv%1007

s=input()
print(solve(s))