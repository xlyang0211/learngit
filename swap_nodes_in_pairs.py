# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        pointer_tmp = head
        node_tmp = head
        if pointer_tmp is None:
            return None
        elif pointer_tmp.next is None:
            return pointer_tmp
        else:
            while pointer_tmp.next is not None:
                if pointer_tmp == head:
                    print "enter"
                    node_tmp = node_tmp.next
                    pointer_tmp.next = node_tmp.next
                    node_tmp.next= pointer_tmp
                    head = node_tmp
                    node_tmp = pointer_tmp
                else:
                    if pointer_tmp.next.next is not None:
                        node_tmp = node_tmp.next # Node 2
                        pointer_tmp.next = node_tmp.next # Node 1 next to Node 3;
                        node_tmp.next = pointer_tmp.next.next # Node 2 next to Node 4;
                        pointer_tmp.next.next = node_tmp
                        pointer_tmp = node_tmp
                    else:
                        return head
                print pointer_tmp.val
            return head

if __name__ == "__main__":
    head = ListNode(0)
    pointer = head
    for i in xrange(1, 9):
        node = ListNode(i)
        pointer.next = node
        pointer = pointer.next
    solution = Solution()
    head = solution.swapPairs(head)
    pointer = head
    while pointer is not None:
        print pointer.val
        pointer = pointer.next

# Summarize this problem:
# 1. Critical knowledge is to manipulate list node: insert, delete and reverse position;
# 2. In python, mutable variable assignment is reference assignment, take care of it;
# 3. Do remember to deal with boundary problem with if else structure:
#    such as: when dealing with head, 3 nodes involved: head, head.next, head.next.next;
#             when dealing with intermediate nodes, 4 nodes involved: node before;
#                                                                     node to be dealt;
#                                                                     node.next
#                                                                     node.next.next