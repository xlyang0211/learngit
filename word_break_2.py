class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return True
        else:
            return self.word_divide_helper(s, dict)

    def word_divide_helper(self, s, dict):
        print "s is:", s
        if len(s) == 0:
            return True
        for item in dict:
            if self.string_start_with(s, item):
                # Here you can not directly return return self.word_divide_helper((s[len(item):]))
                if self.word_divide_helper(s[len(item):], dict): # Please notice the subtlety here, only return True!!!
                    return True
        return False

    def string_start_with(self, s, sub):
        for i in xrange(len(s)):
            if sub == s[:i+1]:
                return True

solution = Solution()
s = "abc"
dict = ["a", "b", "bc", "bbb", "bbbb"]
print solution.wordBreak(s, dict)