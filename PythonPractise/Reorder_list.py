class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        a=[]
        while cur:
            a.append(cur.val)
            cur=cur.next
            
        for i in range(len(a)):
            if i%2!=0:
                a.insert(i,(a[len(a)-1]))
                # a.remove((a[len(a)-1]))
                a.pop()
        
        dummy=cur=ListNode(None)
        for i in a:
            cur.next=ListNode(i)
            cur=cur.next
        
        return dummy.nextr