class Solution:
    def sortByFreq(self,a,n):
        h1={}
        m=[]
        p=[]
        for i in a:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        return sorted(h1.items(), key=lambda kv:[kv[1], kv[0]])
        # for i in t:
        #     for j in range(i[1]):
        #         p.append(i[0])
        # return p
# l=list(map(int,input().split()))
l=[6, 6, 2 ,3 ,1 ,4 ,1 ,5 ,6 ,2 ,8 ,7 ,4 ,2 ,1 ,3 ,4 ,5 ,9 ,6]
obj=Solution()
print(obj.sortByFreq(l,5))