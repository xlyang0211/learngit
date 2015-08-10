__author__ = 'seany'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head is None:
            return head
        else:
            count = 0
            tmp_node = head
            new_head = head
            new_tail = head
            while tmp_node.next:
                if count == k:
                    new_tail = tmp_node
                tmp_node = tmp_node.next
                if count == k:
                    new_head = tmp_node
                count += 1
            tmp_node.next = head
            new_tail.next = None
            return new_head

# Still problem, the system report that [1, 2], 1 results in [1, 2], while I think it's [2, 1];