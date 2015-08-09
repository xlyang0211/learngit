class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        flag = 0
        if n >= 0:
            flag = 1
        else:
            n = -n
        dict = {}
        dict[0] = 1
        dict[1] = x
        i = 2
        sqr = x
        while i < n:
            sqr *= sqr
            dict[i] = sqr
            i *= 2
        print dict
        if flag == 1:
            return self.get_pow(x, n, dict)
        else:
            return 1/self.get_pow(x, n, dict)

    def get_pow(self, x, n, dict):
        print "n is:", n
        if n in dict:
            return dict[n]
        else:
            if n % 2:
                return self.get_pow(x, (n-1)/2,dict) * self.get_pow(x, (n+1)/2,dict)
            else:
                tmp = self.get_pow(x, n/2, dict)
                return tmp * tmp

if __name__ == "__main__":
    n = 9
    solution = Solution()
    print solution.pow(1.26441, n)