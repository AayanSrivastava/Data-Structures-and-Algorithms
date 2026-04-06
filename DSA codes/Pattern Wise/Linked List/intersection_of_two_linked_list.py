class Solution:
    def getIntersectionNode(self, headA, headB):
        cur = headA
        cur1 = headB
        while cur!=cur1:
            if cur:
                cur = cur.next
            else:
                cur = headB
            if cur1:
                cur1 = cur1.next
            else:
                cur1 = headA

        return cur