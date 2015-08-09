class QuickSort:
    def quick_sort(self, list, first, last):
        """
        :param list: The list to be sorted
        :param first: The first index of the list to be sorted
        :param last: The last index of the list to be sorted
        :return: The sorted list
        """
        if first == last:
            return list
        pivot = list[last]
        # i marks the index of the last element which is smaller than pivot
        i = first - 1
        # j marks the index of the last element which is bigger than pivot
        for j in xrange(first, last):
            if list[j] <= pivot:
                list[i+1], list[j] = list[j], list[i+1]
                i += 1
            else:
                pass
        # Here i+1 is the index of first element bigger than pivot (with index of last)
        list[i+1], list[last] = list[last], list[i+1]
        # no need to sort the first half:
        if first >= i:
            # no need to sort the second half:
            if last <= i + 2:
                return list
            # just sort the second half:
            else:
                self.quick_sort(list, i+2, last)
        else:
            # just sort the first half:
            if last <= i + 2:
                self.quick_sort(list, first, i)
            # both half(s) need to be sorted.
            else:
                self.quick_sort(list, first, i)
                self.quick_sort(list, i+2, last)
        return list

if __name__ == "__main__":
    list = [2, 5, 12, 4, 8, 3, 11]
    #list = [1]
    #list = [3, 2]
    list = [2, 3]
    my_quick_sort = QuickSort()
    print my_quick_sort.quick_sort(list, 0, len(list)-1)


