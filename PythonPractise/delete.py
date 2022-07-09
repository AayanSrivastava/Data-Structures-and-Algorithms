# n=int(input())
# a=list(map(int,input().split()))
# return len(a)


# def count(a):
#     h={}
#     for i in a:
#         if i in h:
#             h[i]+=1
#         else:
#             h[i]=1
#     return h

# while (count(a)<=len(a)):
#     for i in count(a):
#         if h[i]>1:
# try1234
# print(len(h))


# m=len(matrix)
# n=len(matrix[0])
# n=3
# m=3
# matrix1 = [[0 for i in range(m)] for j in range (n)]
# print(matrix1)

# points = [[3,3],[5,-1],[-2,4]]
# a=[]
# for i in points:
#     s=0
#     for k in i:
#         s+=abs(k)**2
#     a.append((s,i))
# a.sort(key=lambda x:x[0])
# l1,l2=list(zip(*a))
# print(list(l1))
# print(list(l2)[0:2])

# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(6))
    
# nums=[1,2,3]
# l=[[]]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)+1):
#         l.append(nums[i:j])
# l.sort()
# print(l)

l=[4, 6, 2, 3, 8, 9]
a= reduce (lambda x,y:x^y,l) 
print(a)