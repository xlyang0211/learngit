__author__ = 'seany'

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        row = len(matrix)
        col = row
        real_row = 0
        real_col = 0
        if row % 2:
            real_row = row / 2
            real_col = col / 2 + 1
        else:
            real_row = row / 2
            real_col = col / 2
        for i in xrange(real_row):
            for j in xrange(real_col):
                old_row, old_col = i, j
                new_row, new_col = i, j
                for t in xrange(3):
                    new_row, new_col = self.coordinate_transformation(row, new_row, new_col)
                    matrix[old_row][old_col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[old_row][old_col]

    def coordinate_transformation(self, n, row, col):
        new_row = col
        new_col = n - row - 1
        return new_row, new_col

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3], [2, 4, 8], [3, 6, 9]]
    solution.rotate(matrix)
    print matrix

