class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node):
        data=int(input("Enter the data of node"))
        node=self.createNode(data)
        if data==-1:
           return None
        node.left=self.insert(node.left,data)
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
root=None
l.insert(root)

# l.postorder(root.right)
l.inorder(root)
# l.preorder(root.right)