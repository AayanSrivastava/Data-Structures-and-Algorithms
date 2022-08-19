from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        # data=int(input())
        if node is None:
           return self.createNode(data)
        node.left=self.insert(node.left,data)
        node.right=self.insert(node.right,data)
        return node

    def levord(self,root):
        ans=[]
        if root==None:
            return ans
        q=deque([root])
        while q:
            n=len(q)
            level=[]
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.data)
        ans.append(level)
        print(ans)
                    
                    
    def areAnagrams(self, node1):
        return self.levord(node1)

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
root=l.createNode(1) 
l.insert(root,2)
l.insert(root,3)
l.insert(root,4)
l.insert(root,5)
# l.postorder(root.right)
# l.inorder(root.right)
# l.preorder(root.right)
# print(l.areAnagrams(root))
l.levord(root)