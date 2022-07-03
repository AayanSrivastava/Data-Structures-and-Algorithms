# a,b=input("enter ").split(",")
# print("hello" +" "+ a +" and " + b)
# print("hello {} and {}".format(a,b))
# print(f"hello {a} and {b}")

# a,b=input("enter ").split(",")
# print(f"{len(a)}")
# print(a.lower().count(b.lower()))

# a=input("Enter the IP Address")
# print(a.replace(".","[.]"))
# x=6
# if x>5:
#     pass

# name="Aayan"
# if 'y' in name:
#     print("Present")
# else:
#     print("Absent")
#sum of n natural number
# n=int(input("Enter any natural no."))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

# sum of digits

# n=int(input("Enter no."))
# sum=0
# while n>0:
#     a=n%10
#     sum+=a
#     n//=10
# print(sum)

# n=input("Enter")
# sum=0
# l=len(n)-1
# while l>=0:
#     sum+=int(n[l])
#     l-=1
# print(sum)

# frequency of letters in a word
# name=input("Enter")
# i=0
# t=""
# while i<len(name):
#     if name[i] not in t:
#         t+=name[i]
#         print(f"{name[i]}={name.count(name[i])}")
#     i+=1
# print(t)

# for i in range(20):
#     if i==5:
#         continue
#     if i==8:
#         break
#     print(i)

#number guessing game

# import random
# num=random.randint(1,100)
# guess=int(input("Enter"))
# i=1
# t=False
# while not t:
#     if guess==num:
#         print(f"You won! you guessed it in {i} times")
#         t=True
#     else:
#         if guess>num:
#             print("Too High")
#         else:
#             print("Too Low")

#         i=i+1
#         guess=int(input("Guess again"))

# n="Aayan"
# for i in "Srivas":
#     print(i)

# functions

#function definition
# def add(a,b):    -->parameter
#     return a+b

# function calling
# print(add(10,8))  -->argument

# def wish():
#     return "Happy Birthday"

# print(wish())

# # function inside function
# def palindrome(str):
#     if reverse(str)==str:
#         return "Palindrome"
#     return "Not Palindrome"

# def reverse(s):
#     t=""
#     for i in range(len(s)-1,-1,-1):
#         t+=s[i]
#     return t

# print(palindrome(input())

# #factorial

# def fact(n):
#     f=1
#     for i in range(n,1,-1):
#         f*=i
#     return f
# print(fact(34))
# print(fact(20))

# s=0
# n=int(input("Enter the no."))
# while n>0:
#     a=(n%10)
#     s=(s*10) + a
#     n=n//10
# print(s)

# num=[1,2,3,4]
# print(num,num[2])

# num[1]="aayan"
# print(num)

# print(num[:2])

# num=[1,2,3,4]
# num.append(2)
# print(num)

# num.insert(1,8)
# print(num)

# num1=[5,6,7,8]
# print(num+num1)

# a=[12,34,35,36]
# b=[4,5,6]
# # a.append(b)
# # a.extend(b)
# a.pop(2)
# del a[1]
# a.remove(12)
# print(a)
# print(b)

# n=[1,2,3,4]
# if 1 in n:
#     print("Present")
# else:
#     print("Absent")


# s="aayan srivastava IT Undergraduate KIET Group Of Institutions"
# print(s.split(" "))

# a,b,c=input("Enter value").split(" ")
# print(a +" "+ b +" "+ c)

# info=['aayan','13']
# print(''.join(info))

# def squarelist(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square

# print(squarelist(list(range(1,10))))

# def reverse(l):
#     rev=l[::-1]
#     return rev

# print(reverse(list(range(1,10))))

# a=[1,2,3,4]
# a.reverse()
# print(a)

# a=[1,2,3,4]
# l=[]
# for i in range(len(a)):
#     l.append(a.pop())

# print(l)

# def revlist(l):
#     l1=[]
#     for i in l:
#         l1.append(i[::-1])
#         l1.reverse()
#     return l1

# print(revlist(['abc','xyz','mno']))

# def oddeve(l):
#     odd=[]
#     eve=[]
#     li=[]
#     for i in l:
#         if i%2==0:
#             eve.append(i)
#         else:
#              odd.append(i)
#     li.append(odd)
#     li.append(eve)
#     return li

# print(oddeve(list(range(1,10))))

# a=[1,2,3]
# b=[4,5,6]
# a.append(b)
# print(a)

# def intersect(l1,l2):
#     f=[]
#     for i in l1:
#         if i in l2:
#             f.append(i)
#     return f

# print(intersect(list(range(5)),[3,2,6,4]))

#counting no. of lists inside a list

# l=[1,2,3,[1,2,3],[4,5,6]]
# c=0
# for i in l:
#     if type(i) is int:
#         c=c+1
# print(c)

# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# l=[]
# l1=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i+j+k) != n:
#                 l.append(i)
#                 l.append(j)
#                 l.append(k) 
#                 l1.append(l)
#                 l=[]
# print(l1)

# n=int(input())
# l=input().split()
# l1=[]
# for i in l:
#     l1.append(int(i))
# l1.remove(max(l1))
# print(max(l1))

# s="ABCBCBCBC"
# ss="CB"
# print(s.count(ss))

# s="hello world"
# s=s.split()
# for i in s:
#     if len(i)>1:
#         print(i.title(),end=" ")
#     else:
#         print(i)

# s="1 w 2 r 3g"
# s=s.split()
# t=[]
# s1=" "
# for i in s:
#     if len(i)>2:
#         t.append(i.title())
#     else:
#         t.append(i)
# print(s1.join(t))

# s="1ewq wre 2 r 3g"
# s=s.split()
# for i in s:
#     print(i[0])


# name=input("enter")
# t=""
# i=0
# for i in range(len(name)):
#     if name[i] not in t:
#         t+=name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i=i+1


# s="ramama"
# print(s.replace("a","t",2))

# s="132 456 Wq  m e"
# print(list(s.split(" ")))


# s="fewf"
# for i in s:
#     print(i)

# def bigsorting(l):
# l=['1','56','34','66']
# l.sort()
# print(l)

# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
# for i in sorted(l):
#     print(i)


# l=[]
# n=int(input())
# for i in range(n):
#     l.append(int(input()))

# for i in l:
#     if l.count(i)>1:
#         for k in range(l.count(i)):
#             l.remove(i)
# print(l)


# l=[]
# p=[]
# n=int(input())
# for i in range(n):
#     l.append(int(input()))

# for i in l:
#     s=str(i)
#     for k in s:
#         if s.count(k)>1:
#             print(i)


# n=[6,3,1,8,9,2,10,12,7,4,11]
# s=int(input())
# e=int(input())
# q=[]
# a=[]
# for i in range(len(n)):
#     if n.index(n[i]) in range(s,e):
#         q.append(n[i])
#     else:
#         a.append(n[i])
# q=q[::-1]
# for i in q:
#     a.insert(s,i)
#     s=s+1
# print(a)


# n=[6,3,1,8,9,2,10,12,7,4,11]
# s=int(input())
# e=int(input())
# n[s:e]=n[s:e][::-1]
# print(n)

# s,st=input().split(",")
# s=list(s.split())
# st=list(st.split())
# t=[]
# y=[]
# for i in s:
#     if i in st:
#         pass
#     else:
#         t.append(i)
# for i in st:
#     if i in s:
#         pass
#     else:
#         y.append(i)
# print(' '.join(t))
# print(' '.join(y))

# n=int(input())
# k=int(input())
# l=[]    
# a=[]
# for i in range(n):
#     l.append(int(input()))

# l=[2,7,4,1,9,2,3,10,1,5]
# k=4
# a=[]
# for i in range(1,len(l)-1):
#     if abs(l[i-1]-l[i]) > k and abs(l[i+1]-l[i]) > k:
#         a.append(l[i])
# print(a)


# s=input()
# s=list(s.split())
# a=[]
# q=[]
# c=0
# for i in s:
#     if i==i[::-1]:
#         a.append(i)
#         q.append(s.index(i)+c)
#         s.remove(i)
#         c=c+1
# a.sort()
# print(a)
# print(q)
# for i in range(len(q)):
#     s.insert(q[i],a[i])
# s=' '.join(s)
#  print(s)


# def ugly(n):
#     i=2
#     c=0
#     while n>1:
#         if n%i==0:
#             n=n//i
#             if i>5:
#                 c=c+1
#         else:
#             i=i+1
#     if c==0:
#         return 1
#     return 0
# n=int(input("Enter the number"))
# t=False
# i=2
# d=1
# while not t:
#     if ugly(i):
#         d=d+1
#     i=i+1
#     if d==n:
#         t=True
# print(i-1)


# def ugly(n):
#     i=2
#     l=[]
#     while n>1:
#         if n%i==0:
#             n=n//i
#             l.append(i)
#         else:
#             i=i+1
#     if(l.count(2)+l.count(3)+l.count(5))==len(l):
#         return "true"
#     return "false"
# n=int(input())
# print(ugly(n))

# l=[]
# n=int(input("Enter"))
# for i in range(n):
#     l.append(int(input()))
# for i in l:
#     if not bool(i):
#         l.remove(i)
# print(l)

# swapping two characters simultaneously in a string list
# l=['Gfg','is','best','for','Geeks']
# r=[i.replace('G','.').replace('e','G').replace('.','e') for i in l]
# print(r)

# n=int(input())
# l=[]
# s=[]
# for i in range(n):
#     l.append(int(input()))
# for i in l:
#     sum=0
#     while i>0:
#         a=i%10
#         sum+=a
#         i//=10
#     s.append(sum)
# print(s)


# n=int(input())
# l=[]
# s=[]
# for i in range(n):
#     l.append(int(input()))
# for i in l:
#     sum=0
#     for k in str(i):
#         sum+=int(k)
#     s.append(sum)
# print(s)

# n=int(input())
# l=list(map(int,input().strip().split()))[:n]
# t=l.count(max(l))
# print(t)
# l.sort()
# print(l)
# for i in range(t):
#     l.remove(max(l))
# print(max(l))

# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[i for i in l if i%2==0]
# print(l1)

# n=int(input("Ënter"))
# a=[]
# l=list(map(int,input().strip().split()))[:n]
# for i in l:
#     if l.count(i)>1 and i not in a:
#         a.append(i)
# print(a)

# l=[5,6,[],4,[1,2,3],5,8,[],9]
# for i in l: 
#     if type(i)==list:
#         if len(i)==0:
#             l.remove(i)
# print(l)


# s="my name is aayan . aayan is a good boy . He is a software Engineer"
# s=list(s.split())
# for i in s:
#     if i == 'is':
#         s.remove(i)
# s=' '.join(s)
# print(s)


# import random
# a=random.randint(10,20)
# print(a)
# n=int(input("Ënter "))
# l=[]
# i=2
# while n>1:
#     if n%i==0:
#         n=n//i
#         l.append(i)
#     else:
#         i=i+1
# print(l)

# l=[1,2,3]
# l1=[1,2,8]
# if l==l1:
#     print("yes")
# else:
#     print("no")
# s="lmnop"
# l=[]
# l1=[]
# a=[]
# b=[]
# t=s[::-1]
# for i in s:
#     l.append(ord(i))
# for i in t:
#     l1.append(ord(i))
# for i in range(len(l)-1):
#     a.append(abs(l[i]-l[i+1]))
# for i in range(len(l1)-1):
#     b.append(abs(l1[i]-l1[i+1]))
# if a==b:
#     print("Funny")
# else:
#     print("Not Funny")

# TUPLE
# t=(1,2,3)
# print(type(t))
# print(t[:1])
# print(min(t))
# print(max(t))s


# a=(1,2,[3,4,5],6)
# a[2].append(8)
# print(a)

# print(tuple(range(1,11)))

# a=[1,2,3]
# a=str(a)
# print(a[0])


# l=[1,3,5,6,73,9,8]
# a=[]
# N=int(input())
# for i in range(N):
#     a.append(max(l))
#     l.remove(max(l))
# print(a)
# l.sort(reverse=True)
# print(l)


# l = [1000,298,3579,100,200,-45,900]
# n = 4
  
# l.sort()
# print(l)
# print(l[-2])


# tuples = [('','','8'), (), ('0', '00', '000'), 
#                  ('birbal', '', '45'), (''), (),  ('',''),()]
# for i in tuples:
#     if len(i)==0 and type(i)==tuple:
#         tuples.remove(i)
# print(tuples)

# tuples = [('','','8'), (), ('0', '00', '000'), 
#                  ('birbal', '', '45'), (''), (),  ('',''),()]
# for i in tuples:
#     if not i:
#         print(i)

# print(bool(()))


# l=[10,20,30,44]
# j=0
# a=[]
# for i in l:
#     j+=i
#     a.append(j)
# print(a)

# s=input()
# if len(s)<3:
#     print("empty string")
# else:
#     print(s[:3]+s[-3:])


# s=input()
# s=s[::-1]
# a=[]
# t=list(s.spli t())
# for i in t:
#     a.append(i[::-1])
# a=' '.join(a)
# print(a)
# print(s)



# s=input()
# s=list(s.split())
# l=[]
# for i in s:
#     if i not in l:
#         print(i +":"+str(s.count(i)))
#         l.append(i)

# s=input()
# print(s.replace("_",""))

# s="my name is aayan"
# print(s.split())
# s=input()
# t=""
# for i in s:
#     if s.count(i)>1 and i not in t:
#         t+=i
#         print(i)

# s=input()
# s1=input()
# while s1 in s:
#     s=s.replace(s1,"")
# if len(s)==0:
#     print("Yes")
# else:
#     print("No")

# s=input()
# d=int(input("How much to shift "))
# a=s[d:]+s[:d]
# b=s[-d:]+s[:-d]
# print("Left Rotation:" + a)
# print("Right Rotation:" + b)

# from itertools import permutations
# s="ABC"
# for i in permutations(s):
#     print(''.join(i))

# s=input()
# m=s.find('a')
# print(m)

# l=[1,2,3]
# k=reversed(l)
# print(k)

# l=[1,2,3,4,5]
# a=[]
# k=int(input())
# for i in range(k):
#     a.append(min(l))
#     l.remove(min(l))
# p=len(a)
# for i in range(k):    
#     a.insert(p,max(l))
#     l.remove(max(l))
#     p=len(a)-1  
# print(tuple(a))

# l=[9,5,6]
# a=[]
# for i in l:
#     a.append((i,i**3))
# print(a)

# l=[(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# a=[]
# for i in l:
#     for j in i:
#         if j==l[0]:
#             a.append(i)
# print(a)

# print(ord('A'))

# a=input(input())

# def isprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             ç=c+1
#     if c>0:
# s=12
# print(f"Num: {s}")

# l=[1,2,3,4,5,6]
# print(l[-1:2:2])

# l=[(5,6),(5,7),(5,8),(6,7),(7,8)]
# l1,l2=list(zip(*l))
# for i in range(len(l)-2):
#     if l[i][0]==l[i+1][0]:
#         t=zip(l[i],l[i+1])
# print(list(t))

# t=int(input())
# l=[]
# a=[]
# q=[]
# min=1000
# while t>0:
#     s=input()
#     n = float (input())
#     l.append([s,n])
#     t=t-1
# l.sort(key = lambda x:x[1])
# for i in range(len(l)):
#     if min(list(lambda x :x[1])):
#         a.append(l[i][0])

# print(a)

# t=int(input())
# l=[]
# a=[]
# q=[]
# min=1000
# while t>0:
#     s=input()
#     n = float (input())
#     l.append([s,n])
#     t=t-1
# l1,l2= zip(*l)

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# for i in student_marks:
#     if student_marks.get(query_name):
#         t=sum(student_marks.get(query_name))/3
# print("{:.2f}".format(t))

# def count_substring(string, sub_string):
#     return string.count(sub_string)+string[::-1].count(sub_string)

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# n,x=input().split()
# d={}
# a=[]
# for i in range(int(x)):
#     l=input().split()
#     l=list(map(float,l))
#     a.append(l)
# t=list(zip(*a))
# for i in t:
#     s=float(sum(i)/3)
#     print(s)

# s="web designing"
# print(s[4:10])

# import requests
# page = requests.get("https://www.worldometers.info/coronavirus")
# page.status_code
# page.content
# from bs4 import BeautifulSoup


# t=int(input())
# while t>0:
#     x1,x2,y1,y2,z1,z2=input().split()
#     if int(x2)<int(x1) or int(y2)<int(y1) or int(z2)>int(z1):
#         print("NO")
#     else:
#         print("YES")
#     t=t-1

#     try:
#     t=int(input())
#     while t>0:
#         s=0
#         c=0
#         n=input()
#         l=list(map(int,input().strip().split()))[:int(n)]
#         for i in l:
#             s+=1
#             if i<8:
#                 c+=1
#             if c==7:
#                 break
#         print(s)
#         t-t-1
# except:
#     pass

# q=4
# l=list(map(int,input().strip().split()))[:q]

# n,q=input().split()
# l=list(map(int,input().strip().split()))[:int(n)]
# q=int(q)
# while q>0:
#     s=1
#     x=int(input())
#     for i in l:
#         s*=(x-i)
#     if s==0:
#         print("0")
#     elif s<0:
#         print("NEGATIVE")
#     elif s>0:
#         print("POSITIVE")
#     q=q-1

# l=list(map(int,input("Enter a tuple").split(",")))
# m=[]
# n=[]
# for i in range(2):
#     m.append(min(l))
#     l.remove(min(l))
#     n.append(max(l))
#     l.remove(max(l))
# n.sort()
# print(tuple(m))
# print(tuple(n))


# t=int(input())
# while t>0:
#     A=input()
#     A=list(A)
#     if A[0]!='1':
#         A.insert(0,'1')
#     else:
#         A.insert(1,'0')
#     print(''.join(A))
#     t=t-1

# t=int(input())
# while t>0:
#     a=[]
#     b=[]
#     n=int(input())
#     l=list(map(int,input().strip().split()))[:n]
#     for i in l:
#         if i%2==0:
#             a.append(i)
#         else:
#             b.append(i)
#     for i in (a+b):
#         print(i,end=" ")
#     print("\n")
#     t=t-1


# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# print(fact(34))
# print(fact(100))

# a,b,c=input().split('\n',3)


# l1=([1,2,3],[4,5,6])
# l=[(1,2),(2,3),(3,4)]
# print(list(zip(*l)))

# n=['Aayan','Ram','Shyama']
# print(max(n,key=lambda item : len(item)))

# s2={
#     'aayan': {'score':90,'age':22},
#     'Ram': {'score':80,'age':23},
#     'Shyam': {'score':60,'age':21}
# }

# print(max(s2,key=lambda i : s2[i]['score']))


# s2=[
#     {'name':'aayan','score':90,'age':22},
#     {'name':'ram','score':80,'age':21},
#     {'name':'shyam','score':70,'age':24}
# ]

# print(min(s2,key=lambda i : i.get('score'))['name'])


# s2=[
#     {'name':'aayan','score':90,'age':22},
#     {'name':'ram','score':80,'age':21},
#     {'name':'shyam','score':70,'age':24}
# ]

# print(sorted(s2,key=lambda i : i.get('age'), reverse=True))
# print(sorted(s2,key=lambda i : i['age']))

# import time
# t1=time.time()

# def deco(x):
#     def decoin():
#         print("Executing")
#         return x
#     return decoin


# def func1():
#     print("Executed")

# func1 = deco(func1)
# func1()

# t2=time.time()
# print(t2-t1)

# OOP

# class Student:
#     def __init__(self,fn,ln,age):
#         self.firstname  = fn
#         self.lastname  = ln
#         self.age = age

# p1 = Student('Aayan','Srivastava',22)
# print(p1.lastname)

# class student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         print(self.id)
# std=student("simon",1)
# std.id=2
# print(std.id)

# a=(2,3,1,5)
# a[2] =10
# print(a)



# n = int(input())
# count = 0

# for i in range(1,n+1):
#     m = str(i+i*(i+1)+i*(i+1)*(i+2))
#     summ = 0
#     for digit in str(m):
#         summ = summ + int(digit)
#         sum1 = summ
#     if(summ < 2):
#         print(m)
#     else:
#         for j in range(2, sum1):
#             if(sum1 % j == 0):
#                 print(m)
#                 break
#         else:
#             print(m)
#             print("primesum")
#             count = count + 1

# print("Total prime sum values:",count)


# def fre(s):
#     s=s.lower()
#     t=""
#     d={}
#     for i in s:
#         if i not in t:
#             d[i]=s.count(i)
#             t+=i
#     return d

# s=input()
# print(fre(s))



# x='python'
# y= 'y' in x 
# print(y)

# a=4&5%34**3
# print(a)

# class Laptop:
#     #global variable
#     discount=100
#     def __init__(self,brand,mname,price):
#         #instance variables
#         self.brand = brand
#         self.model_name = mname
#         self.price = price
    
#     def discountprice(self):                         #instance method
#         offprice= (Laptop.discount/100)*self.price
#         return self.price-offprice

# Laptop1=Laptop('hp','au114xt',50000)
# print(Laptop1.discountprice())
# print(Laptop1.__dict__)

# d={'foo':100,'bar':200,'baz':300}
# print(d['bar':'baz'])

# e="helle"
# print(e.rfind("e"))

# for i in (i+5 in range(5)):
#     print(i,end=" ")

# y=8
# z=lambda x:x*y
# print(z(6))

# a="this is programming"
# print(a[2:5:-1])

# FILES I/O

# f=open('file.txt')
# for i in f.readlines()[:1]:
#     print(i)
# f.close()

# with open('file.txt','w') as f:
#     f.write("hello")

# str = '''Welcome to Python Programming
#                 class. Let's learn the concept
#                 of Strings in Python.'''
# print(str)



# s=input()
# sum=0
# for i in s:
#     sum=+(ord(i)-97)

# def isprime(n):
#     for i in range(2,int(n/2)+1):
#         if n%i==0 or n>99:
#             return 0
#         else:
#             return 1

# if isprime(sum):
#     print("Lucky")
# else:
#     print("Unlucky")


# s=int(input())
# hrs=s//3600
# s=s%3600
# mins=s//60
# s=s%60
# secs=s
# print(f"{hrs} hrs {mins} mins {secs} secs")

# string=input()
# def matchparanthesis(s):
#     c,d=0,0
#     for i in s:
#         if i=='(':
#             c=c+1
#         if i==')':
#             d=d+1
#     return c==d
# print(matchparanthesis(string))

# s=tuple(map(int,input().strip().split(",")))
# s=list(s)
# m1=[]
# m2=[]
# for i in range(2):
#     m1.append(min(s))
#     s.remove(min(s))
#     m2.append(max(s))
#     s.remove(max(s))
# m2.sort()
# print(tuple(m1),tuple(m2))


# def twoSum(l,t):
#     y=[]
#     for i in range(len(l)-1):
#         for j in range(i+1,len(l)):
#             if l[i]+l[j]==t:
#                 y.append(l[i])
#                 y.append(l[j])
#                 print(list(y))

# print(twoSum([1,2,3,4],7))
# def hammingWeight(n):
#     n=str(n)
#     n=list(n)
#     return n.count("1")
# print(hammingWeight(100000111))

# s="1234"
# s=int((s))
# print(s)

# class Solution:
#     def numIdenticalPairs(self, nums):
#         hashMap = {}
#         res = 0
#         for number in nums:            
#             if number in hashMap:
#                 res += hashMap[number]
#                 hashMap[number] += 1
#             else:
#                 hashMap[number] = 1
#         return res

# obj= Solution()
# n=[1,2,5,2,3,4.5]
# print(obj.numIdenticalPairs(n))

# class hashmap:
#     def frequency(self,l):
#         hashmap={}
#         r=0
#         for i in l:
#             if i in hashmap:
#                 r+=hashmap[i]
#                 hashmap[i]+=1
#             else:
#                 hashmap[i]=1
#         return hashmap
# l=[0,1,2,3,4,5,6,7,8,2,5]
# obj=hashmap()
# print(obj.frequency(l))

# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str):
#         h1={}
#         h2={}
#         r=0
#         for i in jewels:
#             if i in h1:
#                 h1[i]+=1
#             else:
#                 h1[i]=1
#         for j in stones:
#             if j in h2:
#                 h2[j]+=1
#             else:
#                 h2[j]=1
#         for i in h1:    
#             if i in h2:
#                 r+=h2[i]
#         return r
# obj=Solution()
# j="aA"
# s="aAAbbb"
# print(obj.numJewelsInStones(j,s))

# oneLiner
# sum(map(S.count, J)) = sum( map(lambda x:s.count(x) ,j))

# def numJewelsInStones(self, J, S):
#         setJ = set(J)
#         return sum(s in setJ for s in S)

# class OOP:
#     a=5
#     b=6
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def sum(self):
#         return self.a+self.b
#     @classmethod
#     def sum1(cls):
#         return cls.a
#     @staticmethod
#     def sum2():
#         print("static method")

# obj=OOP()
# print(obj.a)
# print(obj.b)
# print(OOP.a)
# print(obj.sum())
# print(OOP.sum1())
# print(obj.sum2())

# class Solution:
#     def findDuplicates(self, nums):
#         a=[]
#         for i in nums:
#             if nums.count(i)==2:
#                 a.append(i)
#                 del nums[i]
#         return a
# l=[13,8,5,3,20,12,3,20,5,16,9,19,12,11,13,19,11,1,10,2]
# obj=Solution()
# print(obj.findDuplicates(l))

# class Solution:
#     def isIsomorphic(self,s,t):
#         h1={}
#         h2={}
#         h3={}
#         h4={}
#         c=0
#         if len(s)==len(t):
#             for i in s:
#                 if i in h1:
#                     h1[i]+=1
#                 else:
#                     h1[i]=1
#             for i in t:
#                 if i in h2:
#                     h2[i]+=1
#                 else:
#                     h2[i]=1
#             for i in h1.values():
#                 if i in h3:
#                     h3[i]+=1
#                 else:
#                     h3[i]=1

#             for i in h2.values():
#                 if i in h4:
#                     h4[i]+=1
#                 else:
#                     h4[i]=1

            
#             print(h1)
#             print(h2)
#             print(h3)
#             print(h4)
#         if h3==h4:
#             return True
#         else:
#             return False

# s="bbbaaaba"
# t="aaabbbba"
# obj=Solution()
# print(obj.isIsomorphic(s,t))

# def isIsomorphic3(self, s, t):
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# class Solution:
#     def sortSentence(self, s):
#         a=[]
#         s=s.split()
#         s.sort(key=lambda x:x[len(x)-1])
#         for i in s:
#             a.append(i[:len(i)-1])
#         a=' '.join(a)
#         return a

# obj=Solution()
# print(obj.sortSentence("is2 sentence4 This1 a3"))

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         output=[0 for i in range(len(heights))]
#         count=[0 for i in range(101)]
#         for i in range(1,len(heights)):
#             count[heights[i]]+=1
#         for i in range(1,101):
#             count[i]+=count[i-1]
#         for i in range(len(heights)-1,-1,-1):
#             output[count[heights[i]]]=heights[i]
#             count[heights[i]]-=1
#         return output
# l=[1,6,3,8,5]
# c=[0 for i in range(len(l))]
# for i in range(max(l)):
#         c[l[i]]+=1
# print(c)

print("hi")