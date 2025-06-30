def subs(s):
    substring = ""
    for i in range(len(s)):
        sub = ""
        seen = set()
        for j in range(i,len(s)):
            if s[j] in seen:
                break
            sub+=s[j]
            seen.add(s[j])
            if len(sub)>len(substring):
                substring = sub
    print(substring)
s = "geeksforgeeks"
subs(s)