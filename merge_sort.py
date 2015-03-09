#! /usr/bin/python

# -*- coding: utf-8 -*-

def merge(list, head_1, tail_1, head_2, tail_2):
    """ Sorted from minimum to maximum """
    list_new = []
    head_1_tmp = head_1
    while head_1 != tail_1 and head_2 != tail_2:
        if list[head_1] > list[head_2]:
            list_new.append(list[head_2])
            head_2 = head_2 + 1
        else:
            list_new.append(list[head_1])
            head_1 = head_1 + 1
    list_new.extend(list[head_1:tail_1])
    list_new.extend(list[head_2:tail_2])
    list[head_1_tmp: tail_2] = list_new

def merge_sort(list, head, tail):
    mid = int((head + tail)/2)
    if head + 1 < mid:
       merge_sort(list, head, mid)
    if mid + 1 < tail:
        merge_sort(list, mid, tail)
    merge(list, head, mid, mid, tail)

# The main program #
if __name__ == "__main__":
    lst = [23, 432,654, 34, 48, 2398, 202, 2323, 23092, 8, 23, 20, 239, 923, 492, 230]
    print list
    merge_sort(lst, 0, len(lst))
    print lst
