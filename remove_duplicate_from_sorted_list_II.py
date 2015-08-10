__author__ = 'seany'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        my_set = set()
        duplicate = []
        if head is None:
            return []
        else:
            my_set.add(head.val)
        tmp = head
        iter = head.next
        while iter is not None:
            if iter.val in my_set:
                duplicate.append(iter.val)
                tmp.next = iter.next
                iter = iter.next
            else:
                my_set.add(iter.val)
                tmp = tmp.next
                iter = iter.next
        tmp_1 = head
        tmp_2 = head.next
        ret = []
        if tmp_1.val not in duplicate:
            ret.append(tmp_1.val)
        while tmp_2 is not None:
            if tmp_2.val in duplicate:
                tmp_1.next = tmp_2.next
                tmp_2 = tmp_2.next
            else:
                ret.append(tmp_2.val)
                tmp_1 = tmp_1.next
                tmp_2 = tmp_2.next
        return ret

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    solution = Solution()
    print solution.deleteDuplicates(head)

# How to:
# 1. traverse the list and delete duplicate node, except the first duplicate one, but mark the value of duplicate node;
# 2. delete the remain duplicate node;