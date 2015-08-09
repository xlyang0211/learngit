# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        return self.mergeLists(0, len(lists)-1, lists)

    def mergeLists(self, start, end, lists):
        length = end - start + 1
        if length <= 1:
            if length == 0:
                return None
            else:
                return lists[start]
        else:
            if length == 2:
                return self.merge_2_lists(lists[start], lists[end])
            else:
                mid = (start + end) / 2
                return self.merge_2_lists(self.mergeLists(start, mid, lists), self.mergeLists(mid+1, end, lists))

    def merge_2_lists(self, head_1, head_2):
        new_head = None
        ptr_1 = None
        ptr_2 = None
        if head_1.val < head_2.val:
            new_head = head_1
            ptr_1 = head_1.next
            ptr_2 = head_2
        else:
            new_head = head_2
            ptr_1 = head_1
            ptr_2 = head_2.next
        #print "The head is:", new_head.val
        new_ptr = new_head
        while ptr_1 is not None and ptr_2 is not None:
            if ptr_1.val < ptr_2.val:
                new_ptr.next = ptr_1
                ptr_1 = ptr_1.next
            else:
                new_ptr.next = ptr_2
                ptr_2 = ptr_2.next
            new_ptr = new_ptr.next
        if ptr_1 is None:
            if ptr_2 is None:
                return new_head
            else:
                new_ptr.next = ptr_2
                return new_head
        else:
            if ptr_1 is None:
                return new_head
            else:
                new_ptr.next = ptr_1
                return new_head

if __name__ == "__main__":
    lst_1 = [1, 5, 8, 11]
    lst_2 = [5, 99, 110]
    lst_3 = [1, 6, 32, 105, 111]
    head_1 = ListNode(lst_1[0])
    head_2 = ListNode(lst_2[0])
    head_3 = ListNode(lst_3[0])
    ptr_1 = head_1
    ptr_2 = head_2
    ptr_3 = head_3
    for i in lst_1[1:]:
        ptr_1.next = ListNode(i)
        ptr_1 = ptr_1.next
    for i in lst_2[1:]:
        ptr_2.next = ListNode(i)
        ptr_2 = ptr_2.next
    for i in lst_3[1:]:
        ptr_3.next = ListNode(i)
        ptr_3 = ptr_3.next
    lst = [head_1, head_2, head_3]
    solution = Solution()
    head = solution.mergeKLists(lst)
    while head is not None:
        print head.val
        head = head.next