class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def insert(self,root,key):
        if root==None:
            return Node(key)
        elif root.val>key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        return root

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

t=Tree()
# root=t.insert(None,5)
root=Node(5)
t.insert(root,4)
t.insert(root,7)
t.insert(root,2)
t.insert(root,9)
t.inorder(root)