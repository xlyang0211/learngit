def counting_sort(lst, k):
    """
    Realize counting sort
    :param lst: input list
    :return: a sorted list
    """
    # Several conditions for counting sort:
    # all elements in lst are integers;
    # all elements are within [0, k];
    lst_tmp = [0] * k
    result = [0] * len(lst)
    for i in lst:
        lst_tmp[i] += 1
    for i in xrange(1, len(lst_tmp)):
        lst_tmp[i] += lst_tmp[i-1]
    print lst_tmp
    for i in range(len(lst))[::-1]:
        result[lst_tmp[lst[i]]-1] = lst[i]
        lst_tmp[lst[i]] -= 1
    return result

if __name__ == "__main__":
    lst = [1, 9, 7, 2, 0]
    print counting_sort(lst, 10)
