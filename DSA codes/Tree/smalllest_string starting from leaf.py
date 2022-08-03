class Solution:
    def solve(self,root,s,ans):
        if root==None:
            return
        a1=root.val+97
        s+=chr(a1)
        if root.left==None and root.right==None:
            sorted(s)
            s=s[::-1]
            ans.append(s)
        self.solve(root.left,s,ans)
        self.solve(root.right,s,ans)
        
    def smallestFromLeaf(self, root):
        s=""
        ans=[]
        self.solve(root,s,ans)
        ans.sort()
        return ans[0]