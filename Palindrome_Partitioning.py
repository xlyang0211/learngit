__author__ = 'seany'

class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        sub_list = []
        total_list = []
        if len(s) == 0:
            return []
        self.dfs(s, 0, 1, sub_list, total_list)
        return total_list

    def dfs(self, s, begin, end, sub_list, total_list):
        if end == len(s):
            if self.is_palindrome(s[begin: end]):
                total_list.append(sub_list + [s[begin: end]])
        else:
            if self.is_palindrome(s[begin: end]):
                self.dfs(s, end, end+1, sub_list + [s[begin: end]], total_list)
            self.dfs(s, begin, end+1, sub_list, total_list)

    def is_palindrome(self, my_str):
        if my_str[::1] == my_str[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    s = "aba"
    print solution.partition(s)