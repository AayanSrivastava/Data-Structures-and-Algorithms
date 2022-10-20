# from collections import Counter
# a='aaaa'
# b='aaab'
# c=Counter(a)
# d=Counter(b)
# z=c&d
# max1=float('-inf')
# for i in z:
#     if z[i]>max1:
#         max1=z[i]
# print(max1)


from sys import maxsize
 
def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    ar=[]
 
    for i in range(0, size):
        ar.append(a[i])
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    return ar
print(maxSubArraySum([2,3,1],3))