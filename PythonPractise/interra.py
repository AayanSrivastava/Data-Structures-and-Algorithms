# s1=input()
# s2=input()
# s2=s2[:-1]
# t=s1.find(s2)
# if t==-1:
#     print("no matches found")
# else:
#     print(s1[t:])

s=input()
ans=""
for i in range(len(s)):
    if s[i] not in ['a','e','i','o','u','A','E','I','O','U']:
        ans+=s[i]
    else:
        for j in range(i,len(s)-1):
            if s[j] and s[j+1] in ['a','e','i','o','u','A','E','I','O','U',""]:
                ans+=s[j]+s[j+1]
print(ans)