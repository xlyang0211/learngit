__author__ = 'seany'

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 2:
            return []
        matrix = [[0] * n for i in xrange(n)]
        ret = []
        matrix[0][0] = 1
        self.find_proximity(n, 0, 0, matrix, 'a')
        ret.append(self.find_non_zero(matrix))
        matrix[0][0] = 1
        self.find_proximity(n, 0, 0, matrix, 'b')
        ret.append(self.find_non_zero(matrix))
        matrix[0][1] = 1
        self.find_proximity(n, 0, 1, matrix, 'a')
        ret.append(self.find_non_zero(matrix))
        matrix[0][1] = 1
        self.find_proximity(n, 0, 1, matrix, 'b')
        ret.append(self.find_non_zero(matrix))

        matrix[1][0] = 1
        self.find_proximity(n, 1, 0, matrix, 'a')
        ret.append(self.find_non_zero(matrix))
        matrix[1][0] = 1
        self.find_proximity(n, 1, 0, matrix, 'b')
        ret.append(self.find_non_zero(matrix))
        matrix[1][1] = 1
        self.find_proximity(n, 1, 1, matrix, 'a')
        ret.append(self.find_non_zero(matrix))
        matrix[1][1] = 1
        self.find_proximity(n, 1, 1, matrix, 'b')
        ret.append(self.find_non_zero(matrix))
        combinations = []
        for i in ret:
            if len(i) < n:
                pass
            else:
                self.traverse_list(i, 0, n, [], combinations)
        print "combinations is: ", combinations


    def find_proximity(self, n, a, b, matrix, type):
        if type == 'a':
            x = a - 1
            y = b + 2
            if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                if matrix[x][y] != 1:
                    matrix[x][y] = 1
                    self.find_proximity(n, x, y, matrix, type)
            x = a + 2
            y = b + 1
            if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                if matrix[x][y] != 1:
                    matrix[x][y] = 1
                    self.find_proximity(n, x, y, matrix, type)
        if type == 'b':
            x = a + 2
            y = b - 1
            if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                if matrix[x][y] != 1:
                    matrix[x][y] = 1
                    self.find_proximity(n, x, y, matrix, type)
            x = a + 1
            y = b + 2
            if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                if matrix[x][y] != 1:
                    matrix[x][y] = 1
                    self.find_proximity(n, x, y, matrix, type)

    def find_non_zero(self, matrix):
        n = len(matrix)
        ret = []
        for i in xrange(n):
            for j in xrange(n):
                if matrix[i][j] == 1:
                    ret.append([i, j])
                    matrix[i][j] = 0
        return ret

    def traverse_list(self, ret, start, n, sub_list, combinations):
        """
        find all the sub list in ret which contains n element
        Note that there is no duplicate element in n;
        :param ret: list of elements
        :param n: number of elements in sub list;
        :return: list of list;
        """
        if n == 0:
            combinations.append(sub_list)
        else:
            for i in xrange(start, len(ret) - n + 1):
                self.traverse_list(ret, i + 1, n - 1, sub_list + [ret[i]], combinations)




if __name__ == "__main__":
    solution = Solution()
    solution.solveNQueens(5)