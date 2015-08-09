__author__ = 'seany'

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        print m, n
        s = [[0] * n for i in xrange(m)]
        if dungeon[m-1][n-1] >= 0:
            s[0][0] = 1
        else:
            s[0][0] = 1 - dungeon[m-1][n-1]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    if dungeon[m-i-1][n-j-1] >= 0:
                        if dungeon[m-i-1][n-j-1] < s[i][j-1]:
                            s[i][j] = s[i][j-1] - dungeon[m-i-1][n-j-1]
                        else:
                            s[i][j] = 1
                    else:
                        s[i][j] = s[i][j-1] - dungeon[m-i-1][n-j-1]
                elif j == 0:
                    if dungeon[m-i-1][n-j-1] >= 0:
                        if dungeon[m-i-1][n-j-1] < s[i-1][j]:
                            s[i][j] = s[i-1][j] - dungeon[m-i-1][n-j-1]
                        else:
                            s[i][j] = 1
                    else:
                        s[i][j] = s[i-1][j] - dungeon[m-i-1][n-j-1]
                else:
                    if s[i][j-1] >= s[i-1][j]:
                        if dungeon[m-i-1][n-j-1] >= 0:
                            if dungeon[m-i-1][n-j-1] < s[i-1][j]:
                                s[i][j] = s[i-1][j] - dungeon[m-i-1][n-j-1]
                            else:
                                s[i][j] = 1
                        else:
                            s[i][j] = s[i-1][j] - dungeon[m-i-1][n-j-1]
                    else:
                        if dungeon[m-i-1][n-j-1] >= 0:
                            if dungeon[m-i-1][n-j-1] < s[i][j-1]:
                                s[i][j] = s[i][j-1] - dungeon[m-i-1][n-j-1]
                            else:
                                s[i][j] = 1
                        else:
                            s[i][j] = s[i][j-1] - dungeon[m-i-1][n-j-1]
        #return s
        return s[m-1][n-1]

if __name__ == "__main__":
    square = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    # square = [[0,0]]
    solution = Solution()
    for i in solution.calculateMinimumHP(square):
        print i
