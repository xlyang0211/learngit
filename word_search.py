__author__ = 'seany'

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        visited = []
        flag = False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.bfs(board, visited, word, 0, i, j):
                    flag = True
        return flag

    def bfs(self, board, visited, word, index, i, j):
        if index == len(word):
            return True
        else:
            my_flag = False
            row = len(board)
            col = len(board[0])
            if [i, j] not in visited and board[i][j] == word[index]:  # (i, j) has not been visited;
                index += 1
                if index == len(word):
                    my_flag = True
                if 0 <= i - 1 <= row - 1 and self.bfs(board, visited + [[i, j]], word, index, i-1, j):
                    my_flag = True
                if 0 <= j - 1 <= col - 1 and self.bfs(board, visited + [[i, j]], word, index, i, j-1):
                    my_flag = True
                if 0 <= i + 1 <= row - 1 and self.bfs(board, visited + [[i, j]], word, index, i+1, j):
                    my_flag = True
                if 0 <= j + 1 <= col - 1 and self.bfs(board, visited + [[i, j]], word, index, i, j+1):
                    my_flag = True
            return my_flag
            # There should be no else, because if (i, j) is in visited, it should not enter in dealing with (i, j);

if __name__ == "__main__":
    board = ["ABCE", "SFCS", "ADEE"]
    str = "ASFCE"
    solution = Solution()
    print solution.exist(board, str)

# Notice: algorithm above can not pass the online judge of leetcode for time limitation. Pruning is iin necessary!
# Look at the following algorithm with pruning which passed the online judgement:
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        visited = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.bfs(board, visited, word, 0, i, j):
                    return True
        return False

    def bfs(self, board, visited, word, index, i, j):
        if index == len(word):
            return True
        else:
            row = len(board)
            col = len(board[0])
            if [i, j] not in visited and board[i][j] == word[index]:  # (i, j) has not been visited;
                index += 1
                if index == len(word):
                    return True
                if 0 <= i - 1 <= row - 1 and self.bfs(board, visited + [[i, j]], word, index, i-1, j):
                    return True
                if 0 <= j - 1 <= col - 1 and self.bfs(board, visited + [[i, j]], word, index, i, j-1):
                    return True
                if 0 <= i + 1 <= row - 1 and self.bfs(board, visited + [[i, j]], word, index, i+1, j):
                    return True
                if 0 <= j + 1 <= col - 1 and self.bfs(board, visited + [[i, j]], word, index, i, j+1):
                    return True
            return False