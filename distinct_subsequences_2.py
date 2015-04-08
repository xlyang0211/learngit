__author__ = 'seany'

import time
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        l_s = len(S)
        l_t = len(T)
        if l_s < l_t:
            return 0
        m = [[0] * l_s for i in xrange(l_t)]  # m[i][j] denotes the number of sub string T[0:i+1] in S[0:j+1];
        for i in xrange(l_t):
            for j in xrange(i, l_s):
                if i == 0:  # Get the first line of m;
                    if T[i] == S[j]:
                        if j == 0:
                            m[i][j] = 1
                        else:  # if multiple S[j] equals to T[0], the m[i][j] value should equal to the previous one;
                            m[i][j] = m[i][j-1] + 1
                    else:  # if multiple S[j] do'not equals to T[0], the m[i][j] value should equal to the previous one;
                        m[i][j] = m[i][j-1]
                elif i == j:  # Get the diagonal values of m, exclude m[0][0];
                    if T[i] == S[j]:
                        if m[i-1][j-1] == 0:
                            m[i][j] = 0
                        else:
                            m[i][j] = 1
                else:  # Get the value of ordinary places;
                    if T[i] == S[j]:
                        m[i][j] = m[i-1][j-1] + m[i][j-1]
                    else:
                        m[i][j] = m[i][j-1]
        return m[l_t-1][l_s-1]

if __name__ == "__main__":
    S = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    S = "rrrabbbit"
    T = "rabbit"
    solution = Solution()
    a = time.clock()
    print solution.numDistinct(S, T)
    b = time.clock()
    print b - a

# Accepted!
# Dynamic Programming has 2 main key points:
# 1. define the boundary of the table to record intermittent values; (which is discarded in DFS that make DFS
#    has a much bigger time complexity)
# 2. find the transition function, in this problem:
#    m[i][j] = m[i-1][j-1] + m[i][j-1], if T[i] == S[j];
#            = m[i][j-1], if T[i] != S[j];
#    Where m is the record table, m[i][j] denotes that there are m[i][j] T[0:i+1] in S[0:j+1];