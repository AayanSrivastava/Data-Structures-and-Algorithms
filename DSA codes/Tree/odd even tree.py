from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createNode(self,data):
        return TreeNode(data)

    def insert(self,node,data):
        if node is None:
           return self.createNode(data)
        if data < node.val:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node

    def isEvenOddTree(self, root):
        even=[]
        odd=[]
        if root==None:
            return []
        lev=True
        q=deque([root])
        while q:
            n=len(q)
            level=[]
            for i in range(n):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            if lev:
                even.extend(level)
            else:
                odd.extend(level)
            lev=not lev
        od= all(even[i] % 2 == 0 for i in range(len(even)))
        ev= all(odd[i] % 2 != 0 for i in range(len(odd)))
        return odd
l=Solution()
root=TreeNode(1)
l.insert(root,2)
l.insert(root,3)
l.insert(root,4)
l.insert(root,5)
l.insert(root,6)
l.insert(root,7)
print(l.isEvenOddTree(root))