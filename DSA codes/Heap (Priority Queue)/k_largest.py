from heapq import heappop,heapify
k=2
nums=[3,2,1,5,6,4]
heapify(nums)
print(nums)
while len(nums)>k:
    heappop(nums)
print(nums)


# def solve(self, A, B):
#     while len(A)>B:
#         A.remove(min(A))
#     return A

# def solve(self, A, B):
#     A.sort(reverse=True)
#     return A[:B]