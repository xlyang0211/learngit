<<<<<<< HEAD
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
=======
# counting sort requirements:
# 1. all elements are integers within [0, k]

def counting_sort(lst, k):
    """
    Implementing counting sort algorithm
    time complextiy: O(n)
    space complexity: O(n+k)
    :param lst: input a list of integers between 0 and k;
    :param k: the scope of integers in lst;
    :return: a list of sorted integers
    """
    tmp = [0] * k  # tmp is a temporary list;
    result = [0] * len(lst)
    for i in lst:
        tmp[i] += 1
    for i in xrange(1, k):
        tmp[i] += tmp[i-1]
    print "The tmp is:", tmp
    for i in range(len(lst))[::-1]:
        result[tmp[lst[i]]-1] = lst[i]
        tmp[lst[i]] -= 1
        print "The tmp is:", tmp
        print "The result is:", result
    return result

if __name__ == "__main__":
    lst = [8, 3, 23, 22, 4, 18, 11]
    k = 25
    print counting_sort(lst, k)
>>>>>>> 1f33a455313b490408713921ee3fcc8211a33488
