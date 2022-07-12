
def merge(arr,mid):
    a=arr[:mid+1]
    b=arr[mid+1:]
    i=0
    j=0
    k=0
    while i<len(a) and j<len(b):
        if (a[i]<b[j]):
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1

    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1

def mergesort(arr,l,r):
    if l>=r:
        return
    mid=(l+r)//2
    
    mergesort(arr,l,mid)
    mergesort(arr,mid+1,r)
    merge(arr,mid)
    return arr

arr=[2,5,1,6,9]
print(mergesort(arr,0,len(arr)-1))