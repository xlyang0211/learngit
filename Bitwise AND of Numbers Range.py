__author__ = 'xlyang0211'

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        m_bin = bin(m)
        result = ["1"] * (len(m_bin) - 2)
        for i in xrange(m, n):
            residue =  bin(i)[-(len(m_bin) - 2):]
            for j in xrange(len(result)):
                if result[j] == "1" and residue[j] == "0":
                    result[j] = "0"
        return int("".join(result), 2)



if __name__ == "__main__":
    solution = Solution()
    print solution.rangeBitwiseAnd(0, 2147483647)