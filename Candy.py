class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        mark = 0
        sum = 0
        previous = 0
        length = len(ratings)
        if length == 1:
            return 1
        for i in xrange(length):
            if i == 0:
                if ratings[i] <= ratings[i+1]:
                    sum += 1
                    previous = 1  # The previous is the current rating value and "previous" for next node!
                else:
                    sum += 2
                    previous = 2
                    mark = i
            elif i == length - 1:
                if ratings[i] > ratings[i-1]:
                    sum += previous + 1
                    previous += 1
                elif ratings[i] == ratings[i-1]:
                    #  What if neighbour's rating score are the same?
                    sum += previous
                    #  Here we adopted the scheme that same score get same candy
                else:
                    if previous == 1:
                        sum += (i - mark + 1)
                        previous = 1
                    else:
                        sum += 1
                        previous = 1
            else:
                if ratings[i-1] < ratings[i]:
                    sum += previous + 1
                    previous += 1
                    if ratings[i] >= ratings[i+1]:
                        mark = i
                elif ratings[i-1] == ratings[i]:
                    sum += previous  # No changes to previous
                else:
                    if previous == 1:
                        sum += (i - mark + 1)  # All previous nodes add 1
                        previous = 1
                    else:
                        if previous > 2:
                            mark = i
                        sum += 1
                        previous = 1
        return sum

if __name__ == "__main__":
    lst = [1, 3, 2, 5, 3, 3, 2, 1]
    lst = [1, ]
    solution = Solution()
    print solution.candy(lst)


#   --_  ------------- Here a mark is placed because it is a local summit;
#_--   --_
#         --_
#            --_
#               ___ -----Here a mark is placed because drop more than 1 happened;
#                  --_
#