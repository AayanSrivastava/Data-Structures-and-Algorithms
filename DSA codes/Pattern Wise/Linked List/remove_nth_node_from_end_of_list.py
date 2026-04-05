# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pos = 0
        while cur:
            cur = cur.next
            pos+=1
        
        remove_i = pos-n
        cur = dummy
        while remove_i:
            cur = cur.next
            remove_i-=1

        cur.next = cur.next.next

        return dummy.next


# Optimised - use two pointer , maintain a gap of n between the two
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next