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
        print("\n")

    def middle(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
    
    def loop(self,head):
        slow,fast=head,head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return 1
        return 0

    def removeloop(self,head):
        slow,fast=head,head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while (slow.next != fast.next):
                    slow=slow.next
                    fast=fast.next
                fast.next = None  # Remove loop
  


l1 = linked()
l1.addNode(10) 
l1.addNode(2) 
l1.addNode(60) 
l1.addNode(35) 
l1.addNode(50) 
l1.printList(l1.head)
# l1.middle(l1.head)
l1.head.next.next.next=l1.head
l1.removeloop(l1.head)
print(l1.loop(l1.head))