import pprint
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        l_lcs = 0  # define l_lcs as the length of longest common substring of word1 and word2;
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        m = len(word1)
        n = len(word2)
        # matrix[m][n] denotes the length of lcs of first m characters of word1 and first n characters of word2;
        matrix = [[0] * (n+1) for i in xrange(m+1)]
        for i in xrange(m+1):
            matrix[i][0] = i
        for j in xrange(n+1):
            matrix[0][j] = j
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+1)
        pprint.pprint(matrix)
        return matrix[m][n]

if __name__ == "__main__":
    s1 = "abcda"
    s2 = "bdabcddsed"
    solution = Solution()
    print solution.minDistance(s1, s2)