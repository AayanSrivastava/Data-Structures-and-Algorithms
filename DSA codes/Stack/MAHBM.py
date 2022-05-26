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
    def NSL(self,arr):
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

    def NSR(self,arr):
        st1 = stack()
        righti = stack()
        for i in range(len(arr)-1,-1,-1):
            if st1.size()==0:
                righti.push1(len(arr))
            elif st1.size()>0 and st1.top()[0]<arr[i]:
                righti.push1(st1.top()[1])
            elif st1.size()>0 and st1.top()[0]>=arr[i]:
                while st1.size()>0 and st1.top()[0]>=arr[i]:
                    st1.pop()
                if st1.size()==0:
                    righti.push1(len(arr))
                else:
                    righti.push1(st1.top()[1])
            st1.push(arr[i],i)
        return righti.display()[::-1]

    # print(NSR(arr))
    # print(NSL(arr))
    def MAH(self,arr):
        width = stack()
        for i in range(len(arr)):
            width.push1(self.NSR(arr)[i]-self.NSL(arr)[i]-1)
        
        width = width.display()
        area = stack()
        for i in range(len(arr)):
            area.push1(width[i]*arr[i])

        area = area.display()
        return max(area)
        #OPTIMIZED
        # n=len(arr)
        
        # left=self.NSL(arr)
        # right=self.NSR(arr)
        
        # width=[right[i]-left[i]-1 for i in range(n)]
        # area=[arr[i]*width[i] for i in range(n)]
        
        # return max(area)

    def MAHBM(self,matrix):
        # aq=[]
        # ar=[]
        # arMAH=0
        # for column in range(len(matrix[0])):
        #     ar.append(matrix[0][column])
        # arMAH = self.MAH(ar)
        # aq.append(arMAH)
        # for row in range(1,len(matrix)):
        #     for column in range(len(matrix[0])):
        #         if matrix[row][column]==0:
        #             ar[column]=0
        #         else:
        #             ar[column]+=int(matrix[row][column])
        #     aq.append(self.MAH(ar))
        #     arMAH = max(arMAH,self.MAH(ar))

        # return arMAH

        rows=len(matrix)
        cols=len(matrix[0])
        hist_arr=[0]*cols
        for col in range(cols):
            hist_arr[col]=int(matrix[0][col])
        print(hist_arr)
        mx=self.MAH(hist_arr)
        for row in range(1,rows):
            for col in range(cols):
                if int(matrix[row][col]) == 0:
                    hist_arr[col]= 0
                else:
                    hist_arr[col]+=int(matrix[row][col])
            print(hist_arr)
            mx=max(mx,self.MAH(hist_arr))
        return mx

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