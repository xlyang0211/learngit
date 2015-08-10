__author__ = 'seany'

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        # greedy algorithm
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s == "0":
                return 0
            else:
                return 1
        num_list = [0] * len(s)
        for i in xrange(len(s)):
            j = len(s) - i - 1
            if i == 0:
                if s[j] != "0":
                    num_list[i] = 1
            else:
                if 10 <= int(s[j: j+2]) <= 26:
                    if i == 1:
                        num_list[i] += 1
                    else:
                        num_list[i] += num_list[i-2]
                if 1 <= int(s[j]) <= 9:
                    num_list[i] += num_list[i-1]
        return num_list[len(s)-1]


if __name__ == "__main__":
    solution = Solution()
    s = "10"
    print solution.numDecodings(s)

# Explanation:
# 1. This problem could be solved with greedy algorithm and think it as below:
# 2. let's say s[2:-1] has n2 combinations, s[1:-1] has n1 combinations;
# 3. if s[0:2] is is between 10 and 26, s[0: -1] has n2 combinations;
# 4. if s[0:1] is between 1 and 9, s[0: -1] has n1 combinations;
# 5. if neither of circumstance above, s[0: -1] has 0 combinations;
# e.g.: s[0:2] = "40", there is 0 combinations for s[0: -1];