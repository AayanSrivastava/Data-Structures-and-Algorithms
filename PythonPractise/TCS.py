# n=int(input())
# ar=list(map(int,input().split()))
# c=0
# for i in range(len(ar)):
#     if ar[i]!=ar[0]:
#         c+=1
# print(c)

# n=int(input())
# points=[]
# for i in range(n):
#     x,y=map(int,input().split())
#     points.append([x,y])
# a = [None] * n
# for i in range(n):
#     x = points[i][0]
#     y = points[i][1]
#     a[i] = max(abs(x), abs(y))

# a.sort()
# index = n // 2 - 1
# print("Minimum M required is:", a[index])

# s=input()
# i=0
# ns=""
# while i<len(s):
#     c=s[i]
#     i+=1
#     count=1
#     while i<len(s) and c==s[i]:
#         count+=1
#         i+=1
#     ns+=c+str(count)
# if len(ns)<len(s):
#     print("Yes")
# else:
#     print("No")
# print(count)