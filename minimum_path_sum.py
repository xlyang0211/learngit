__author__ = 'seany'
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        path = [[0] * col for i in xrange(row)]
        # deal with edge
        path[0][0] = grid[0][0]
        for i in xrange(1, row):
            path[i][0] = path[i-1][0] + grid[i][0]
        for j in xrange(1, col):
            path[0][j] = path[0][j-1] + grid[0][j]
        print path
        for i in xrange(1, row):
            for j in xrange(1, col):
                path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]
        print path
        return path[row-1][col-1]

if __name__ == "__main__":
    grid = [[1, 2], [1, 1]]
    solution = Solution()
    print solution.minPathSum(grid)