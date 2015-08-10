__author__ = 'seany'
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if matrix[0][0] > target or matrix[row-1][col-1] < target:
            return False
        row_1 = 0
        row_2 = row - 1
        while True:
            if row_1 == row_2:
                break
            mid = (row_1 + row_2) / 2
            if target <= matrix[mid][col-1]:
                row_2 = mid
            else:
                row_1 = mid + 1
        col_1 = 0
        col_2 = col - 1
        print row_1
        if target < matrix[row_1][0] or target > matrix[row_1][col-1]:
            return False
        while True:
            if col_1 + 1 == col_2:
                if matrix[row_1][col_1] < target < matrix[row_1][col_2]:
                    return False
                else:
                    return True
            elif col_1 == col_2:
                if matrix[row_1][col_1] == target:
                    return True
                else:
                    return False
            mid = (col_1 + col_2) / 2
            if target <= matrix[row_1][mid]:
                col_2 = mid
            else:
                col_1 = mid + 1

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 1], [3, 3]]
    print solution.searchMatrix(matrix, 2)