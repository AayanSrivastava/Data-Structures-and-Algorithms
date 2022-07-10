from collections import defaultdict


class S:
    def mapp(self,s,h):
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        return h
        
    def groupAnagrams(self, strs):
        a=[]
        h={}
        l=[]
        for i in range(len(strs)):
            h1={}
            self.mapp(strs[i],h1)
            a.append((strs[i],h1))
        for i in range(len(a)):
            s=[]
            for j in range(i,len(a)):
                if a[i][1]==a[j][1]:
                    s.append(a[j][0])
            l.append(s)
        return l

l=S()
a= ["eat","tea","tan","ate","nat","bat"]
print(l.groupAnagrams(a))