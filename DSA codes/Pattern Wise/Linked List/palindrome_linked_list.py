class Solution:
    def isPalindrome(self, head):
        slow = fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next

        prev = None        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        first, second = head, prev
        while first and second:
            if first.val!=second.val:
                return False
            first = first.next
            second = second.next
        return True