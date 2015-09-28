__author__ = 'seany'
import pprint
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        print row, col
        max_square = [[0] * col for i in xrange(row)]
        for i in xrange(row):
            if matrix[i][0] == '1':
                max_square[i][0] = 1
        for j in xrange(col):
            if matrix[0][j] == '1':
                max_square[0][j] = 1
        pprint.pprint(max_square)
        ret = 0
        for i in xrange(row):
            for j in xrange(col):
                if i == 0 or j == 0:
                    if max_square[i][j] > ret:
                        ret = max_square[i][j]
                elif matrix[i][j] == '1':
                    max_square[i][j] = min(max_square[i - 1][j], max_square[i][j - 1], max_square[i - 1][j - 1]) + 1
                    if max_square[i][j] > ret:
                        ret = max_square[i][j]
        pprint.pprint(max_square)
        return ret

if __name__ == "__main__":
    solution = Solution()
    matrix = ["1"]
    print solution.maximalSquare(matrix)