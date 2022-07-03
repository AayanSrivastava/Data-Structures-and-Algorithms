left=[]
right=[]
s=0
minrl=0
height=[0,1,0,2,1,0,1,3,2,1,2,1]
for i in range(len(height)):
    left.append(height[0:i])
    right.append(height[i+1:len(height)])
    # minrl=min(maxl,maxr)
    print(max(left),max(right),minrl)