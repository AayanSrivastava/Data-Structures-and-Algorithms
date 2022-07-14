def sort(a,n):
    if(n==1):
        return

    t=a[-1]
    a.pop()
    sort(a,n-1)
    insert(a,t)
    return a
    
def insert(a,t):
    if (len(a) ==0 or a[-1]<=t):
        a.append(t)
        return
    
    val=a[-1]
    a.pop()
    insert(a,t)
    a.append(val)
    return

arr=[3,5,2,7,1,6]
n=6
print(sort(arr,n))