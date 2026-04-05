def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for i in range(left-1):
            cur = cur.next
        prev = cur

        cur = prev.next
        for j in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next