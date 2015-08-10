__author__ = 'seany'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        head_1 = ListNode(0)
        tmp_1 = head_1
        tmp_1.next = head
        head_2 = ListNode(0)
        tmp_2 = head_2
        while tmp_1.next is not None:
            if tmp_1.next.val >= x:
                tmp_2.next = tmp_1.next
                tmp_2 = tmp_2.next
                tmp_1.next = tmp_1.next.next
            else:
                tmp_1 = tmp_1.next
        tmp_1.next = head_2.next
        tmp_2.next = None
        return head_1.next

# Used to partition list into 2 parts, the former part have values less than x, latter part have values equal or bigger
# than x, the algorithm above get passed once, that's amazing!!!