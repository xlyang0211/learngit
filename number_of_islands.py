__author__ = 'xlyang0211'

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        num_island = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == "1":
                    num_island += 1
                    self.dfs(i, j, grid)
        return num_island

    def dfs(self, i, j, grid):
        row = len(grid)
        col = len(grid[0])
        grid[i][j] = "2"
        if 0 <= i - 1 <= row - 1 and grid[i - 1][j] == "1":
            self.dfs(i - 1, j, grid)
        if 0 <= i + 1 <= row - 1 and grid[i + 1][j] == "1":
            self.dfs(i + 1, j, grid)
        if 0 <= j - 1 <= col - 1 and grid[i][j - 1] == "1":
            self.dfs(i, j - 1, grid)
        if 0 <= j + 1 <= col - 1 and grid[i][j + 1] == "1":
            self.dfs(i, j + 1, grid)

# This problem is almost the same with the matrix of 'X' and 'O' and find the isolated islands of 'O', just turn the
# visited 'O's into other character, such as 'Y' can prevent re-visited. (instead of using a new flag maxtrix to mark
# those grids visited, this method changes the original matrix to mark the visited positions).