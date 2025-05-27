from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root):
        q=[]
        mapper=defaultdict(lambda: defaultdict(list))
        q.append([root,0,0])
        while q:
            node,x,y=q.pop(0)
            if node==None:
                continue
            mapper[x][y].append(node.val)
            q.append((node.left,x-1, y+1 ))
            q.append((node.right,x+1, y+1))

        res= []
        for x in sorted(mapper):
            output=[]
            for y in sorted(mapper[x]):
                output.extend(sorted(mapper[x][y]))
            res.append(output)
        return res
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    print(obj.verticalTraversal(root))