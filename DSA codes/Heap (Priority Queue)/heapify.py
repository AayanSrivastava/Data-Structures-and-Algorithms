# def max_heapify(arr,i):
#     n=len(arr)
#     while i<n//2:
#         left,right=(2*i)+1,(2*i)+2
        
#         # largest so far is compared with left child
#         largest=left if left<n and arr[left]>arr[i] else i

#         # largest so far is compared with right child    
#         largest=right if right<n and arr[right]>arr[largest] else largest

#         # change parent
#         if largest==i:
#             break
#         arr[i],arr[largest]=arr[largest],arr[i]
#         i=largest

# USING RECURSION

# def max_heapify(arr,i):
#     n=len(arr)
#     largest=i
#     left,right=(2*i)+1,(2*i)+2
    
#     # largest so far is compared with left child
#     if left<n and arr[left]>arr[largest]:
#         largest=left

#     # largest so far is compared with right child    
#     if right<n and arr[right]>arr[largest]:
#         largest=right

#     # change parent
#     if largest!=i:
#         arr[i],arr[largest]=arr[largest],arr[i]
#         max_heapify(arr,largest)

# MIN HEAP

def min_heapify(arr,i):
    n=len(arr)
    smallest=i
    left,right=(2*i)+1,(2*i)+2
    
    # largest so far is compared with left child
    if left<n and arr[smallest]>arr[left]:
        smallest=left

    # largest so far is compared with right child    
    if right<n and arr[smallest]>arr[right]:
        smallest=right

    # change parent
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        min_heapify(arr,smallest)


# BUILD HEAP O(N)
arr=[2,66,30,5,9,10]
for i in range((len(arr)//2) - 1,-1,-1):
    # max_heapify(arr,i)
    min_heapify(arr,i)

print(arr)