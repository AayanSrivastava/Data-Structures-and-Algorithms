t=int(input())
while t:
    mat=[]
    for j in range(2):
        a=list(map(int,input().split()))
        mat.append(a)
    if mat[0][0]<mat[0][1] and mat[1][0]<mat[1][1] and mat[0][0]<mat[1][0] and mat[0][1]<mat[1][1]:
        print("YES")
    else:
        print("NO")
    t-=1