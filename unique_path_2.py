class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        # The first solution: dp
        # Define path[i][j] is number of path that can go from coordinates (0, 0) to (i, j).
        m = len(obstacleGrid)  # number of rows
        n = len(obstacleGrid[0])  # number of col
        path = [[0] * n for i in xrange(m)]
        flag_row = 1
        flag_col = 1
        for i in xrange(m):
            if obstacleGrid[i][0] == 1:
                path[i][0] = 0
                flag_row = 0
            else:
                path[i][0] = flag_row
        for j in xrange(n):
            if obstacleGrid[0][j] == 1:
                path[0][j] = 0
                flag_col = 0
            else:
                path[0][j] = flag_col
        print path
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    path[i][j] == 0
                else:
                    path[i][j] = path[i][j-1] + path[i-1][j]
        return path[m-1][n-1]


if __name__ == "__main__":
    obstacleGrid = [
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    obstacleGrid = [[1, 0]]
    solution = Solution()
    print solution.uniquePathsWithObstacles(obstacleGrid)