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
        count = 0
        front_pointer = head
        current_pointer = head.next
        while current_pointer is not None:
            self.insert(head, count, front_pointer, current_pointer)
            count += 1
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
            if new_count == 0:
                pointer = pointer.next
            else:
                pointer_ahead = pointer_ahead.next
                pointer = pointer.next
            new_count += 1

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next = ListNode(1)
    head.next = ListNode(2)
    solution = Solution()
    head = solution.insertionSortList(head)
    print head.val, head.next.val, head.next.next.val, head.next.next.next.val


