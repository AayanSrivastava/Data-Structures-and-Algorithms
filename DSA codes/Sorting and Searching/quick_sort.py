def partition(arr,l,r):
    pivot=arr[l]
    i=0
    j=r-1
    while i<j:
        while arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[l],arr[j]=arr[j],arr[l]
    return j

def quicksort(arr,l,r):
    if l<r:
        p = partition(arr,l,r)
        quicksort(arr,l,p)
        quicksort(arr,p+1,r)

arr=[10,7,8,9,1,5]
print(quicksort(arr,0,len(arr)))
print(arr)