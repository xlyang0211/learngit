class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        lst = ""
        result = []
        self.dfs(0, 0, n, lst, result)
        return result

    def dfs(self, flag, count, n, lst, result):
        if count == n:
            if flag == 0:
                pass
            else:
                result.append(lst+")"*flag)
        else:
            if flag == 0:
                self.dfs(flag+1, count+1, n, lst+"(", result)
            else:
                self.dfs(flag+1, count+1, n, lst+"(", result)
                self.dfs(flag-1, count, n, lst+")", result)

if __name__ == "__main__":
    solution = Solution()
    n = 4
    print solution.generateParenthesis(n)