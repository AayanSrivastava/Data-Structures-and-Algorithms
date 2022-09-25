class Solution():
    def heapify(self,arr,i):
        n=len(arr)
        largest=i
        left,right=(2*i)+1,(2*i)+2
        
        # largest so far is compared with left child
        if left<n and arr[left]>arr[largest]:
            largest=left
    
        # largest so far is compared with right child    
        if right<n and arr[right]>arr[largest]:
            largest=right
    
        # change parent
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,largest)
            
    def mergeHeaps(self, a, b, n, m):
        a.extend(b)
        for i in range((n+m)//2 -1,-1,-1):
            self.heapify(a,i)
        return a