class getNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def hasPath(root, arr,l):
    if root==None:
        return False
    
    arr.append(root.data)
    if root.data==l:	
        return True
	
    if (hasPath(root.left, arr,l) or
		hasPath(root.right, arr,l)):
        return True
    arr.pop(-1)

def printPath(root):
    arr=[]
    # l=[]
    hasPath(root,arr,5)
    return arr

if __name__ == '__main__':
	root = getNode(1)
	root.left = getNode(2)
	root.right = getNode(3)
	root.left.left = getNode(4)
	root.left.right = getNode(5)
	root.right.left = getNode(6)
	root.right.right = getNode(7)
	printPath(root)