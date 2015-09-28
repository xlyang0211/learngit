__author__ = 'seany'

# This problem is still under developing. A better scheme is needed;


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass

    def dfs(self, s, index):
        exp = 0
        if index == len(s):
            return exp
        if s[index] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            tmp = index
            while s[tmp] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                tmp += 1
                if tmp >= len(s):
                    break
            exp += int(s[index: tmp])
            if tmp == len(s):
                return exp
            else:
                return exp + self.eval(s, tmp)
        elif s[index] == " ":
            return self.eval(s, index + 1)
        elif s[index] == "+":
            return exp + self.eval(s, index + 1)
        elif s[index] == "-":
            return exp - self.eval(s, index + 1)
        elif s[index] == "(":
            return self.eval(s, index + 1)
        elif s[index] == ")":
            return self.dfs(s, index + 1)

    def eval(self, s, index, exp):
        mark = 1
        if index == len(s):
            return exp
        while s[index] not in ["(", ")"]:
            if s[index] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                tmp = index
                while s[tmp] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    tmp += 1
                    if tmp >= len(s):
                        break
                if mark:
                    exp += int(s[index: tmp])
                else:
                    exp -= int(s[index: tmp])
                if tmp == len(s):
                    break
                index = tmp + 1
            elif s[index] == " ":
                index += 1
                pass
            elif s[index] == "+":
                mark = 1
                index += 1
            elif s[index] == "-":
                mark = 0
                index += 1
        print exp
        self.eval(s, index + 1, exp) # if another ( ... ) comes, evaluate its value first;

if __name__ == "__main__":
    solution = Solution()
    s = "65 + 82  - (12 + 13 - (24 - 1)) + 1"
    print solution.eval(s, 0, 0)