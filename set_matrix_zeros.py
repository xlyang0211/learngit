__author__ = 'seany'
import pprint
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if len(matrix) == 0:
            pass
        row = len(matrix)
        col = len(matrix[0])
        flag_row = False # Mark if there are zeros in first row;
        flag_col = False # mark if there are zeros in first column;
        pprint.pprint(matrix)
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    if i == 0 and matrix[0][j] == 0: # Why need i == 0: Look explanation below
                        print "j is:", j
                        print "i, j are:", (i, j)
                        flag_row = True
                    if j == 0 and matrix[i][0] == 0:
                        print "i is:", i
                        print "i, j are:", (i, j)
                        flag_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        pprint.pprint(matrix)
        for i in xrange(1, row):
            for j in xrange(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        #pprint.pprint(matrix)
        print flag_row, flag_col
        if flag_row:
            for j in xrange(col):
                matrix[0][j] = 0
        if flag_col:
            for i in xrange(row):
                matrix[i][0] = 0
        pprint.pprint(matrix)


if __name__ == "__main__":
    matrix = [[3,5,5,6,9,1,4,5,0,5],[2,7,9,5,9,5,4,9,6,8],[6,0,7,8,1,0,1,6,8,1],[7,2,6,5,8,5,6,5,0,6],[2,3,3,1,0,4,6,5,3,5],[5,9,7,3,8,8,5,1,4,3],[2,4,7,9,9,8,4,7,3,7],[3,5,2,8,8,2,2,4,9,8]]
    solution = Solution()
    solution.setZeroes(matrix)

# if there is no i == 0 judgement, then when there are 2 or more 0 in certain column apart from the first one, errors
# will occur; actually, we do not need matrix[0][j] after i == 0, right ?!