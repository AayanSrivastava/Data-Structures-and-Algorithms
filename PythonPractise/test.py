# a=[1,2,3,4]
# for i in range(0,len(a)-1,2):
#     a[i],a[i+1]=a[i+1],a[i]
# print(a)


# a=[2,4,5]
# res = int("".join(map(str, a))) #to make a list of numbers into a single integer
# print(res)

# a=[1,2,3,4,5]
# b=[]
# for i in range((len(a)//2)+1):
#         b.append(a[i])
#         if a[len(a)-i-1] not in b:
#             b.append(a[len(a)-i-1])
# print(b)


# a=[1,2,3,4,5,6,7]
# b=[]
# for i in range(len(a)):
#     b.append([a[i:i*1+1]])
#     i=i*1+1
# print(b)

# s="two double one nine triple six eight one six four six zero"
# d={"zero":'0',
#         "one":'1',
#         "two":'2',
#         "three":'3',
#         "four":'4',
#         "five":'5',
#         "six":'6',
#         "seven":'7',
#         "eight":'8',
#         "nine":'9'
#     }
# ap=[]
# s=s.split()
# for i in range(len(s)):
#     if s[i]=='double':
#         for k in range(1):
#             ap.append(d[s[i+1]])
#     elif s[i]=='triple':
#         for k in range(2):
#             ap.append(d[s[i+1]])
#     else:
#         ap.append((d[s[i]]))
# ap=''.join(ap)
# print(str(ap))


# nums=[1,1,1,2,2,3,4]
# h={}
# a=[]
# k=2
# for i in nums:
#     if i in h:
#         h[i]+=1
#     else:
#         h[i]=1

# for i in h:
#     a.append((i,h[i]))
# a.sort(key=lambda x:x[1],reverse=True)
# l1,l2=list(zip(*a))

# print((l1)[:k])
# for i in (h.values()):
#     a.append((i,h[i]))
# print(sorted(h)[:k])
# print(a)
# for i in sorted(h)[:k]:
# nums=["1","2","3"]
# nums=list(map(int,nums))
# print(nums)

# words = ["i","love","leetcode","i","love","coding"]
# k=2
# h={}
# a=[]
# for i in words:
#     if i in h:
#         h[i]+=1
#     else:
#         h[i]=1

# for j in h:
#     a.append((j,h[j]))
        
    # a.sort(key=lambda x:x[1],reverse=True)
    
    # l1,l2=list(zip(*a))
# print(h)
# print(a)
# print(l1)
# print(l2)
# print(l1[:k])

# votes=["ABC","ACB","ABC","ACB","ACB"]
# a=[]
# for i in votes:
#     a.append()
            
# h={}
# for i in a:
#     if i in h:
#         h[i]+=1
#     else:
#         h[i]=1

# b=[]
# for i in h:
#     b.append((i,h[i]))
# print(b)

# a=[2,1,5]
# b=[]
# for i in range(len(a)-1):
# 	t=max(a[i+1:len(a)])
# 	b.append(t)
# b.append(0)
# print(b)

# a=[1,2,3,4,5,6,7,8]
# f=2
# c=[]
# for i in range(0,9,f+1):
#     b=[]
#     b.append(a[i:f])
#     c.append(b)
# print(c)

# a=[1,2,3,4]
# for i in range(len(a)):
#     if i%2!=0:
#         a.insert(i,(a[len(a)-1]))
#         # a.remove((a[len(a)-1]))
#         a.pop()
# print(a)

# for i in range(-1,-5,-1):
#     print(i,end=" ")
# words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# a=[]
# for i in words:
#     h={}
#     for j in i:
#         if j in h:
#             h[j]+=1
#         else:
#             h[j]=1
#     a.append(h)
# for i in a:

# print(a)

n=int(input())
a=list(map(int,input().split(" ")))

dummy=
b=list(a)
if a==b:
    print("Hannah will get treat")
else:
    print("Clay will get treat")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Hannahclay(head):
        cur = head
        a=[]
        while cur:
            a.append(cur.val)
            cur = cur.next
            
        dummy= cur = ListNode(0)
obj=Solution
n=int(input())
a=list(map(int,input().split(" ")))
print(obj.Hannahclay(a))