def totaldig(n):
    if n < 10:
        return c
    if n>=10:
        c+=1
        return totaldig(n%10)