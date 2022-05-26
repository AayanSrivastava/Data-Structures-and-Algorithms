class stack:
    def __init__(self):
        self.container=[]

    def push(self,val,x):
        self.container.append((val,x))

    def push1(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def top(self):
        if self.container:
            return self.container[-1]
        else:
            return None

    def is_empty(self):
        if self.container:
            return len(self.container)==0
        else:
            return None
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container

class Solution:
    def MAHBM(matrix):
        def MAH(arr):
            def NSL(arr):
                st = stack()
                lefti = stack()
                for i in range(len(arr)):
                    if st.size()==0:
                        lefti.push1(-1)
                    elif st.size()>0 and st.top()[0]<arr[i]:
                        lefti.push1(st.top()[1])
                    elif st.size()>0 and st.top()[0]>=arr[i]:
                        while st.size()>0 and st.top()[0]>=arr[i]:
                            st.pop()
                        if st.size()==0:
                            lefti.push1(-1)
                        else:
                            lefti.push1(st.top()[1])
                    st.push(arr[i],i)
                return lefti.display()

            def NSR(arr):
                st1 = stack()
                righti = stack()
                for i in range(len(arr)-1,-1,-1):
                    if st1.size()==0:
                        righti.push1(-1)
                    elif st1.size()>0 and st1.top()[0]<arr[i]:
                        righti.push1(st1.top()[1])
                    elif st1.size()>0 and st1.top()[0]>=arr[i]:
                        while st1.size()>0 and st1.top()[0]>=arr[i]:
                            st1.pop()
                        if st1.size()==0:
                            righti.push1(-1)
                        else:
                            righti.push1(st1.top()[1])
                    st1.push(arr[i],i)
                return righti.display()[::-1]

            # print(NSR(arr))
            # print(NSL(arr))
            width = stack()
            for i in range(len(arr)):
                width.push1(NSR(arr)[i]-NSL(arr)[i]-1)
            
            width = width.display()
            # print(width)

            area = stack()
            for i in range(len(arr)):
                area.push1(width[i]*arr[i])

            area = area.display()

            # print(area)
            return max(area)

        aq=[]
        ar=[]
        arMAH=0
        for column in range(len(matrix[0])):
            ar.append(matrix[0][column])
        arMAH = MAH(ar)
        aq.append(arMAH)
        for row in range(1,len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column]==0:
                    ar[column]=0
                else:
                    ar[column]+=matrix[row][column]
            aq.append(MAH(ar))
            arMAH = max(arMAH,MAH(ar))

        return aq

obj=Solution
r=int(input())
c=int(input())
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

print(obj.MAHBM(matrix))
# a=[6,2,5,4,5,1,6]
# print(obj.MAH(a))