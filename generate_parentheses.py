class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.str_list = []
        str = ''
        self.generate_result_list(n, n, str)

    def generate_result_list(self, left_brace_count, right_brace_count, str):
        if left_brace_count == right_brace_count == 0:
            self.str_list.append(str)
            return self.str_list
        if left_brace_count > 0:
            self.generate_result_list(left_brace_count-1, right_brace_count, str+'(')
        if left_brace_count < right_brace_count and right_brace_count > 0:
            self.generate_result_list(left_brace_count, right_brace_count-1, str+')')

if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(5)
    for str in solution.str_list:
        print "The output str is:", str