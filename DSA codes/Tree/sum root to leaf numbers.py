class Solution:
    def solve(self,root,s,ans):
        if root==None:
            return
        s+=str(root.val)
        if root.left==None and root.right==None:
            ans.append(s)
        
        self.solve(root.left,s,ans)
        self.solve(root.right,s,ans)
        
    def sumNumbers(self, root):
        s=""
        ans=[]
        self.solve(root,s,ans)
        ans=list(map(int,ans))
        return sum(ans)