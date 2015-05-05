import re
class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        flag_digit = 0
        flag_e = 0
        flag_dot = 0
        if len(s) == 0:
            return False
        for i in s:
            if re.match(r'\d', i):
                flag_digit += 1
            elif re.match(r' ', i):
                pass
            elif re.match(r'e', i):
                flag_e += 1
            elif re.match(r'\.', i):
                print "enter here"
                flag_dot += 1
            else:
                return False
        if flag_e and flag_dot:
            return False
        elif s[-1] == "." or s[0] == "e" or s[-1] == "e":
            return False
        elif flag_e > 1 or flag_dot > 1:
            return False
        else:
            if flag_digit:
                return True
            else:
                return False


if __name__ == "__main__":
    s = "1"
    solution = Solution()
    print solution.isNumber(s)