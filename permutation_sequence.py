__author__ = 'seany'

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        digit_list = []
        for i in xrange(1, n + 1):
            digit_list.append(i)
        ret = []
        self.get_digit(n, k, digit_list, ret)
        ret_str = ""
        for i in ret:
            ret_str += str(i)
        return ret_str

    def get_digit(self, n, k, digit_list, ret):
        print(n, ret)
        if n == 1 or k == 0:
            ret.extend(digit_list)
        else:
            if self.factorial(n - 1) < k <= self.factorial(n):
                digit = (k - 1) / self.factorial(n - 1)
                ret.append(digit_list[digit])
                del digit_list[digit]
                self.get_digit(n - 1, k - digit * self.factorial(n - 1), digit_list, ret)
            else:
                ret.append(digit_list[0])
                del digit_list[0]
                self.get_digit(n - 1, k, digit_list, ret)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            if n > 0:
                return n * self.factorial(n - 1)

if __name__ == "__main__":
    n = 5
    k = 4
    solution = Solution()
    print solution.getPermutation(n, k)

# Skill learned:
# 1. how to transfer number sequence into index correspondence:
#     such as:
#     1 ... 6 --- 1
#     7 ... 12 --- 2
#     13 ... 18 --- 3
#     ...
# The code is (n - 1) / 6 + 1, the critical point is differentiate 6 an 7;
