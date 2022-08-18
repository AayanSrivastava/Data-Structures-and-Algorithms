class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    
class linked:
    def __init__(self):
        self.head=None

    def addNode(self,val):
        if self.head==None:
            self.head = Node(val)
            return


        curr = self.head
        while curr.next!=None:
            curr=curr.next

        newNode = Node(val)
        curr.next = newNode

    def printList(self,n):
        while (n != None):
            print(n.data, end=" ")
            n = n.next


l1 = linked()
l1.addNode(10) 
l1.addNode(2) 
l1.addNode(60) 
l1.addNode(35) 
l1.addNode(50) 
l1.printList(l1.head)