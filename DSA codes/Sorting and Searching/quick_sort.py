def quicksort(arr,l,r):
    if l>=r:
        return
    
    p = partition(arr,l,r)

    quicksort(arr,l,p-1)
    quicksort(arr,p+1,r)
    return arr

def partition(arr,l,r):
