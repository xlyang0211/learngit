__author__ = 'seany'

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        direction = 0
        ret = []
        row = len(matrix)
        if row == 0:
            return ret
        col = len(matrix[0])
        if col == 0:
            return ret
        self.dfs(direction, 0, 0, row, col, matrix, ret)
        return ret

    def dfs(self, direction, x, y, row, col, matrix, ret):
        print (x, y)
        if direction == 0:
            for i in xrange(y, y + col, 1):
                ret.append(matrix[x][i])
            x += 1
            y = y + col - 1
            row -= 1
        elif direction == 1:
            for i in xrange(x, x + row, 1):
                ret.append(matrix[i][y])
            x = x + row - 1
            y -= 1
            col -= 1
        elif direction == 2:
            for i in xrange(y, y - col, -1):
                ret.append(matrix[x][i])
            x -= 1
            y = y - col + 1
            row -= 1
        else:
            for i in xrange(x, x - row, -1):
                ret.append(matrix[i][y])
            x = x - row + 1
            y += 1
            col -= 1
        direction = (direction + 1) % 4
        if row != 0 and col != 0:
            self.dfs(direction, x, y, row, col, matrix, ret)

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13,14, 15, 16]]
    print solution.spiralOrder(matrix)