__author__ = 'seany'

import pprint
import sys
print sys.setrecursionlimit(5000)

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        row = len(board)
        if row <= 2:
            return
        col = len(board[0])
        if col <= 2:
            return
        for i in xrange(row):
            self.dfs(i, 0, row, col, board)
            self.dfs(i, col-1, row, col, board)
        for j in xrange(col):
            self.dfs(0, j, row, col, board)
            self.dfs(row-1, j, row, col, board)
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == "D":
                    board[i] = board[i][:j] + "O" + board[i][j+1:]
                elif board[i][j] == "O":
                    board[i] = board[i][:j] + "X" + board[i][j+1:]

    def dfs(self, i, j, row, col, board):
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != "O":
            pass
        else:
            board[i] = board[i][:j] + "D" + board[i][j+1:]
            if 0 <= i-1 <= row-1:
                self.dfs(i-1, j, row, col, board)
            if 0 <= i+1 <= row-1:
                self.dfs(i+1, j, row, col, board)
            if 0 <= j-1 <= col-1:
                self.dfs(i, j-1, row, col, board)
            if 0 <= j+1 <= col-1:
                self.dfs(i, j+1, row, col, board)

if __name__ == "__main__":
    solution = Solution()
    board = [
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
	    "OOOOOOOOOOOOOOOOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	    "XXXXOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
	    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	    "XXXXOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
	    "XOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
    solution.solve(board)
    for i in board:
        print i

# if board is big enough, the problem of 'maximum recursion depth exceeded in cmp' will occur;
# There is no need to remove duplicate as when certain address is 'O' and can be reached from edge, it will be set 'D'
# after visiting it. And it will not be visited again as it's no longer 'O' any more;