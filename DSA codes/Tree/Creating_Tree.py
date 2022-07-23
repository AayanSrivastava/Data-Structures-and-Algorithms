class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None:
           return self.createNode(data)
        if data < node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def preorder(self,root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)       
            print(root.data)
    
l=Tree()
root=l.createNode(0) 
l.insert(root,1)
l.insert(root,2)
l.insert(root,4)
l.insert(root,3)
l.insert(root,5)
# l.postorder(root.right)
l.inorder(root.right)
# l.preorder(root.right)