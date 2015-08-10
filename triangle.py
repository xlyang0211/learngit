__author__ = 'seany'

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        height = len(triangle)
        if height == 0:
            return 0
        elif height == 1:
            return triangle[0][0]
        else:
            for i in reversed(xrange(height - 1)):
                print i
                for j in xrange(i+1):
                    triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

if __name__ == "__main__":
    solution = Solution()
    triangle = [[-1],[2,3],[1,-1,-3]]
    print solution.minimumTotal(triangle)