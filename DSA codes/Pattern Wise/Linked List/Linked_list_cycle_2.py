class Solution:
    def detectCycle(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Step 3: Find the start of the cycle
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer
        
        return None

# 2nd solution 
class Solution:
    def detectCycle(self, head):
        seen = set()
        cur = head
        if head == None:
            return None
        while cur:
            if cur in seen:
                return cur
            else:
                seen.add(cur)
            cur = cur.next
        return None