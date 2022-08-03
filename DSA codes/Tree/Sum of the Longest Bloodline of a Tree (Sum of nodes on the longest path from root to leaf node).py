from collections import defaultdict
class Solution:
    def solve(self,root,l,s,mapper):
        if root==None:
            return
        s+=root.data
        if root.left==None and root.right==None:
            mapper[l].append(s)
        
        self.solve(root.left,l+1,s,mapper)
        self.solve(root.right,l+1,s,mapper)

    def sumOfLongRootToLeafPath(self,root):
        mapper=defaultdict(list)
        self.solve(root,0,0,mapper)
        for i in sorted(mapper,reverse=True):
            mapper[i].sort(reverse=True)
            return mapper[i][0]