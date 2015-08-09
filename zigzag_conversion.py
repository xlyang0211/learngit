class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        s_new = [None] * len(s)
        len_s = len(s)
        col = len_s
        two_dimension_list = [([None]*col) for i in xrange(nRows)]
        for i in xrange(len_s):
            num = i / (nRows-1)
            res = i % (nRows-1)
            x = 0
            y = 0
            if num % 2 == 0:
                x = num/2*(nRows-1)
                y = res
            else:
                x = (num-1)/2*(nRows-1) + res
                y = nRows - res - 1
            two_dimension_list[y][x] = s[i]
        result = ""
        for m in xrange(nRows):
            for n in xrange(col):
                if two_dimension_list[m][n] is not None:
                    result = result + two_dimension_list[m][n]
        return result


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    solution = Solution()
    print solution.convert(s, 4)