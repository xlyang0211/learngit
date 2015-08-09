import numpy
import pprint
import array

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = [] # use list to simulate a stack;
        Bool = [False] * len(s)
        count = 0
        max_len = 0
        for i in xrange(len(s)):
            if s[i] == "(":
                stack.append(i) # stack stores index, it's very important here!!!
            elif s[i] == ")":
                if len(stack) != 0:
                    if s[stack[-1]] == "(":
                        Bool[i] = True
                        Bool[stack[-1]] =True
                        stack.pop()
                    else: # There is no possibility to enter here!!!
                        stack = []
        for item in Bool:
            if item is True:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 0
        max_len = max(max_len, count)
        return max_len

if __name__ == "__main__":
    # The boundary need to use the 0 index, and the real index need to begin from 1, take care of it!!!
    solution = Solution()
    str = "()"
    print solution.longestValidParentheses(str)

#  Summary:
#  1. The problem could be solved with dynamic programming, but with difficulties:
#       - it's not so easy to detect the non-continual valid parentheses;
#       - To distinguish the non-continual and continual valid parentheses, more effort need to do;
#  2. Pay attention to line 15, it's tricky to store "("'s index other than itself;
#  3. The fundamental is that: use a stack to store those left parenthesis which are not paired temporarily
#  4. When right parenthesis find its left parenthesis in the stack, it mark both of their position as True in Bool.
#     This is the tricky part of the algorithm;
#  4. Don't count the length of valid parentheses at first traverse, just mark valid parentheses
#  5. Wait until all are marked and count the number of continual True;