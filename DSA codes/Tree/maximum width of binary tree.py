from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        q=deque([(root,0)])
        width=0
        while q:
            _,left=q[0]
            _,right=q[-1]
            width=max(width,right-left+1)
            
            next_level=deque()
            while q:
                node,index=q.popleft()
                if node.left!=None:
                    next_level.append((node.left,index*2+1))
                if node.right!=None:
                    next_level.append((node.right,index*2+2))
            q= next_level
        return width

# METHOD-2
# def getMaxWidth(self,root):
#     if root is None:
#         return 0
#     q = deque([root])
#     maxWidth = 0
#     while q:
#         n=len(q)
#         maxWidth=max(n,maxWidth)
    
#         while n:
#             n-=1
#             temp=q.popleft()
#             if temp.left:
#                 q.append(temp.left)
#             if temp.right:
#                 q.append(temp.right)
#     return maxWidth