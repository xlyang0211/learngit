__author__ = 'seany'

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        return self.search_matrix(0, row, 0, col, target, matrix)

    def search_matrix(self, r_start, r_end, c_start, c_end, target, matrix):
        r_mid = (r_start + r_end) / 2
        c_mid = (c_start + c_end) / 2
        print r_start, r_end, c_start, c_end
        print r_mid, c_mid
        if r_start + 1 >= r_end and c_start + 1 >= c_end:
            if matrix[r_mid][c_mid] == target:
                return True
            else:
                return False
        if matrix[r_mid][c_mid] == target:
            return True
        elif matrix[r_mid][c_mid] > target:
            print "enter 1"
            flag_1 = self.search_matrix(r_start, r_mid, c_start, c_mid, target, matrix)
            flag_2 = self.search_matrix(r_mid, r_end, c_start, c_mid, target, matrix)
            flag_3 = self.search_matrix(r_start, r_mid, c_mid, c_end, target, matrix)
            return flag_1 or flag_2 or flag_3
        else:
            print "enter 2"
            flag_1 = self.search_matrix(r_mid, r_end, c_mid, c_end, target, matrix)
            flag_2 = self.search_matrix(r_mid, r_end, c_start, c_mid, target, matrix)
            flag_3 = self.search_matrix(r_start, r_mid, c_mid, c_end, target, matrix)
            return flag_1 or flag_2 or flag_3

if __name__ == "__main__":
    matrix = [[0, 1, 2],
              [2, 3, 4],
              [5, 9 , 11],
              [6, 10, 20]]
    matrix= [[-1, 3]]
    solution = Solution()
    print solution.searchMatrix(matrix, 1)