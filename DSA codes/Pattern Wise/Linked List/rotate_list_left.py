class Solution:
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head
        tail = head
        cnt = 1
        while tail.next:
            tail = tail.next
            cnt+=1
        
        k = k % cnt
        if k == 0:
            return head
            
        tail.next = head
        kth = k
        new_tail = head
        while kth>1:
            kth-=1
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head