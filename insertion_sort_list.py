# This algorithm realizes sort a linked list using insert sort;
# And the hard nut is:
# to locate the position to insert into, you need to move index every time, and the head may change after every
# insertion;


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 1
        front_pointer = head
        current_pointer = head.next
        while current_pointer is not None:
            if current_pointer.val < front_pointer.val:
                head = self.insert(head, count, front_pointer, current_pointer)
            # position may change and this will not work!
            # front_pointer = front_pointer.next
            # current_pointer = current_pointer.next
            count += 1
            flag_front_pointer = 0
            front_pointer = head
            while flag_front_pointer != count - 1:
                front_pointer = front_pointer.next
                flag_front_pointer += 1
            current_pointer = front_pointer.next
        return head

    def insert(self, head, count, front_pointer, current_pointer):
        pointer = head
        pointer_ahead = head
        new_count = 0
        while new_count != count:
            if current_pointer.val < pointer.val:
                if pointer is head:
                    front_pointer.next = current_pointer.next
                    current_pointer.next = pointer
                    head = current_pointer
                else:
                    front_pointer.next = current_pointer.next
                    pointer_ahead.next = current_pointer
                    current_pointer.next = pointer
                break
            if new_count == 0:
                pointer = pointer.next
            else:
                pointer_ahead = pointer_ahead.next
                pointer = pointer.next
            new_count += 1
        return head

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(0)
    solution = Solution()
    head = solution.insertionSortList(head)
    pointer = head
    while pointer is not None:
        print pointer.val
        pointer = pointer.next


