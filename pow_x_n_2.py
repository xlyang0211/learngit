class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        else:
            if n % 2:
                return pow(x, n/2)*pow(x, n/2)*x
            else:
                return pow(x, n/2)*pow(x, n/2)

if __name__ == "__main__":
    n = 9
    solution = Solution()
    print solution.pow(1.26441, n)