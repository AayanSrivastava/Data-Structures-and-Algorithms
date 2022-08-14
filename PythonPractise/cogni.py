class sol:
    @classmethod
    def maxon(cls,input1,input2):
        max1=0
        c=0
        one=input2.count(1)
        for i in range(input1):
            if input2[i]==0:
                c+=1
            else:
                c=0
            max1=max(max1,c)
        return (max1+one)
l=sol()
input1=5
input2=[1,0,1,1,1]
print(l.maxon(input1,input2))

# select e.EMPID,e.EMPNAME,d.DEPTID,d.DEPTNAME
# from EMPLOYEE_INFO e,DEPT_INFO d
# where d.DEPTNAME IS NOT NULL;

# select name count(*) from course group by name where term==3;