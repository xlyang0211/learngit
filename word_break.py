class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) < 1:
            return True
        else:
            return self.bfs(s, dict)

    def bfs(self, s, dict):
        if len(s) == 0:
            return True
        if s in dict:
            return True
        for i in (1, len(s)):
            if s[:i] in dict:
                if self.bfs(s[i:], dict):  # This step is critical, because dfs only need to get one result to exit.
                    return True
        return False

solution = Solution()
s = "bac"
dict = ["ac", "b", "bbbb", "bbb", "bbbb"]
print solution.wordBreak(s, dict)

# This solution works from the prospective of the string. It deep first search the string, comparing to the method
# used in word_break_2.py, which dfs the dict instead of the string.
# The word_break_3.py is a new method.