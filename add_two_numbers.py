# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        return_list = ListNode(0)
        pointer = return_list
        if l1.next == None:
            if l2.next == None:
                return return_list
            else:
                return l2
        else:
            if l2.next == None:
                return l1
            else:
                carry = 0
                bit_sum = 0
                addtion_1 = 0
                addtion_2 = 0
                l1_pointer = l1
                l2_pointer = l2
                while l1_pointer.next != None or l2_pointer.next != None:
                    if l1_pointer.next != None:
                        addtion_1 = l1_pointer.next.val
                    else:
                        addtion_1 = 0
                    if l2_pointer.next != None:
                        addtion_2 = l2_pointer.next.val
                    else:
                        addtion_2 = 0
                    bit_sum = addtion_1 + addtion_2 + carry
                    if bit_sum > 10:
                        bit_sum -= 10
                        carry = 1
                    else:
                        carry = 0
                    pointer.next = ListNode(bit_sum)
                    pointer = pointer.next
                    l1_pointer = l1_pointer.next
                    l2_pointer = l2_pointer.next
                return return_list
#  The algorithm is not finished, please refer to the Leetcode for requirements to finish it.


