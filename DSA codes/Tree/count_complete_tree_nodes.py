from collections import deque
class Solution:
    def countNodes(self, root) -> int:
        ans = []
        if root == None:
            return 0
        
        c = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                c+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return c