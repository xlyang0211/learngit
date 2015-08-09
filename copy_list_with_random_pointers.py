# coding: utf-8
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # 这题的难点是：对于random的指针，我怎么知道它指向的是哪一个node，因为指针指向node并无下标作为记号，而只能从头开始；
        pointer = head.next
        new_head = RandomListNode(head.label)
        head.next = new_head
        new_head.random = head
        new_pointer = new_head
        while pointer is not None:
            origin_pointer = pointer
            new_pointer.next = RandomListNode(pointer.label)
            new_pointer.next.random = pointer
            pointer = pointer.next
            origin_pointer.next = new_pointer.next
            new_pointer = new_pointer.next  # This is the key point, please make sure that new_pointer.next exist!!!

        pointer = new_head
        while pointer is not None:
            # pointer.random = pointer.random.random.next
            pointer.random = pointer.random.random.next
            pointer = pointer.next
        new_pointer = new_head
        while new_pointer is not None:
            new_pointer = new_pointer.next
        return new_head

if __name__ == "__main__":
    # Original linked list is constructed as below:
    # 4 nodes are 1, 3, 5, 7;
    # node 1 random to node 5;
    # node 3 random to node 3;
    # node 5 random to node 5;
    # node 7 random to node 3;
    lst = [1, 3, 5, 7]
    head = RandomListNode(lst[0])
    pointer = head
    for i in lst[1:]:
        pointer.next = RandomListNode(i)
        pointer = pointer.next
    new_pointer = head
    pointer_1 = head
    pointer_1.random = pointer_1.next.next
    pointer_1.next.random = pointer_1.next
    pointer_1.next.next.random = pointer_1.next.next
    pointer_1.next.next.next.random = pointer_1.next
    solution = Solution()
    new_head = solution.copyRandomList(head)
    new_pointer = new_head
    while new_pointer is not None:
        print "node:", new_pointer.label,
        print " rand:", new_pointer.random.label
        new_pointer = new_pointer.next

# find out what does it mean:
# pointer = pointer.next
# pointer = ListNode()
# Does this get a linked list???

# Python does not seem to be appropriate to write linked list!!!