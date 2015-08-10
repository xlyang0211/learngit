__author__ = 'seany'

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, n):
        direction = 0
        matrix = [[0] * n for i in xrange(n)]
        if n == 0:
            return matrix
        row = n
        col = n
        num = 1
        self.dfs(direction, 0, 0, row, col, matrix, num)
        return matrix

    def dfs(self, direction, x, y, row, col, matrix, num):
        if direction == 0:
            for i in xrange(y, y + col, 1):
                matrix[x][i] = num
                num += 1
            x += 1
            y = y + col - 1
            row -= 1
        elif direction == 1:
            for i in xrange(x, x + row, 1):
                matrix[i][y] = num
                num += 1
            x = x + row - 1
            y -= 1
            col -= 1
        elif direction == 2:
            for i in xrange(y, y - col, -1):
                matrix[x][i] = num
                num += 1
            x -= 1
            y = y - col + 1
            row -= 1
        else:
            for i in xrange(x, x - row, -1):
                matrix[i][y] = num
                num += 1
            x = x - row + 1
            y += 1
            col -= 1
        direction = (direction + 1) % 4
        if row != 0 and col != 0:
            self.dfs(direction, x, y, row, col, matrix, num)

if __name__ == "__main__":
    solution = Solution()
    print solution.spiralOrder(3)