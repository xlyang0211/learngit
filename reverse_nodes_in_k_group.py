# This is a seemingly easy, very hard actually problem:
# 1. You have to deal with different situations with different k:
#    if k = 1, no change need to be done to the singly_linked_list;
#    if k = 2, to avoid cross boundary, 2 pointers: pointer_1, pointer_2 are used;
#    if k = 3, to avoid cross boundary, 3 pointers: pointer_1, pointer_2, pointer_3 are used;
#    for k = 3, bear in mind that iteration times is equal to k - 3;
# 2. Is there a uniform method to deal with so many if else branches, as it's a big problem in solving this
#    kind of problems in leetcode. Boundary is always the hardest part to solve the problem!


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # First to judge if there are k nodes from this head:
        head = self.reverse_k_element_of_list(head, head, k)
        return head

    def reverse_k_element_of_list(self, pseudo_head, real_head, k):
        """ Here it's guaranteed that there are no less than k element
        :param pseudo_head:
        :param real_head:
        :return: head - The head after reversing k elements;
                 new_pseudo_head - The pseudo_head for another k elements to reverse:
        The image depiction is as below:
        Let's assume k euqals to 3
                        head -> node_1 -> node_2 -> node_3 -> node_4 -> node_5 ...
                          |                 |          |
        group             1                 2          2      ...
        head             head                         head    ...
        pseudo_head   pseudo_head       pseudo_head           ...
        """
        pointer = real_head
        if real_head is None:
            return None
        try:
            for x in xrange(k):
                pointer = pointer.next
        except AttributeError:
            return real_head
        pointer_1 = real_head
        pointer_2 = real_head
        pointer_3 = real_head
        if pseudo_head == real_head: # denotes that this is the real head of the list
            if k == 1:
                self.reverse_k_element_of_list(pointer_1, pointer_1.next, k)
                return pointer_1
            elif k == 2:
                pointer_2 = pointer_2.next
                pointer_1.next = pointer_2.next
                pointer_2.next = pointer_1
                self.reverse_k_element_of_list(pointer_1, pointer_1.next, k)
                return pointer_2
            else:
                pointer_2 = pointer_1.next
                pointer_3 = pointer_2.next
                for i in xrange(k-3):
                    pointer_2.next = pointer_1
                    pointer_1 = pointer_2
                    pointer_2 = pointer_3
                    pointer_3 = pointer_3.next
                real_head.next = pointer_3.next
                pointer_2.next = pointer_1
                pointer_3.next = pointer_2
                self.reverse_k_element_of_list(real_head, real_head.next, k)
                return pointer_3
        else: #pseudo_head is the node before a sub list
            if k == 1:
                self.reverse_k_element_of_list(pointer_1, pointer_1.next, k)
                return pointer_1
            elif k == 2:
                pointer_2 = pointer_1.next
                pseudo_head.next = pointer_2
                pointer_1.next = pointer_2.next
                pointer_2.next = pointer_1
                self.reverse_k_element_of_list(pointer_1, pointer_1.next, k)
                return pointer_2
            else:
                pointer_2 = pointer_1.next
                pointer_3 = pointer_2.next
                for i in xrange(k-3):
                    pointer_2.next = pointer_1
                    pointer_1 = pointer_2
                    pointer_2 = pointer_3
                    pointer_3 = pointer_3.next
                real_head.next = pointer_3.next
                pointer_2.next = pointer_1
                pointer_3.next = pointer_2
                pseudo_head.next = pointer_3
                self.reverse_k_element_of_list(real_head, real_head.next, k)
                return pointer_3


if __name__ == "__main__":
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    #head.next.next.next.next.next = ListNode(6)
    solution = Solution()
    head = solution.reverseKGroup(head, 3)
    while head.next is not None:
        print head.val
        head = head.next
    print head.val