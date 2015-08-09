# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        a_count = 0
        a_point = headA
        b_count = 0
        b_point = headB
        if headA == None or headB == None:
            return None
        while a_point.next != None:
            a_point = a_point.next
            a_count += 1
        while b_point.next != None:
            b_point = b_point.next
            b_count += 1
        if a_point == b_point:
            diff = a_count - b_count
            pseudo_head_a = headA
            pseudo_head_b = headB
            if diff > 0:
                while diff != 0:
                    pseudo_head_a = pseudo_head_a.next
                    diff -= 1
            elif diff < 0:
                diff = 0 - diff
                while diff != 0:
                    pseudo_head_b = pseudo_head_b.next
                    diff -= 1
            while pseudo_head_a != pseudo_head_b:
                pseudo_head_a = pseudo_head_a.next
                pseudo_head_b = pseudo_head_b.next
            return pseudo_head_a
        else:
            return None

if __name__ == "__main__":
    headA = ListNode(0)
    headB = ListNode(0)
    a_point = headA
    b_point = headB
    for i in [5, 4, 9, 3, 4]:
        a_point.next = ListNode(i)
        a_point = a_point.next
    for i in [4, 8, 14, 2, 7, 20, 50]:
        b_point.next = ListNode(i)
        b_point = b_point.next
    for i in [333, 555, 666, 111]:
        node = ListNode(i)
        a_point.next = node
        a_point = a_point.next
        b_point.next = node
        b_point = b_point.next
    # The solution
    solution = Solution()
    print solution.getIntersectionNode(headA, headB).val


