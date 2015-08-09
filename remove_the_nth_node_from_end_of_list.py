# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    # For this problem ,which weird is that no extra invalid header node is used, different from
    # the convention of definition of singly linked list.
    def removeNthFromEnd(self, head, n):
        ptr_a = head
        ptr_b = head
        pre_a = head
        for i in xrange(n-1):
            ptr_b = ptr_b.next
        while ptr_b.next is not None:
            pre_a = ptr_a
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
        if pre_a == ptr_a: # dealing with these boundary conditions are always more difficult than
                           # devising an algorithm.
            head = head.next
        else:
            pre_a.next = pre_a.next.next
        return head

if __name__ == "__main__":
    head = ListNode(0)
    ptr = head
    for i in xrange(1, 10):
        ptr.next = ListNode(i)
        ptr = ptr.next
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, 4)
    new_ptr = new_head
    while new_ptr.next != None:
        print new_ptr.next.val
        new_ptr = new_ptr.next
