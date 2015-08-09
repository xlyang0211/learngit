class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        lst = []
        count = 0
        for i in xrange(0, len(s)-9):
            sub = s[i:i+10]
            self.find_sub_string(count, sub, i, s, lst)
        return lst

    def find_sub_string(self, count, sub, index, s, lst):
        """
        find if sub string exists in s[index:]
        :param count: number of sub have found in s[:index]
        :param sub: the 10 char sub strings;
        :param index: mark the scope of s to be searched;
        :return: None
        """
        if count > 1:
            if sub not in lst:
                lst.append(sub)
        else:
            index = self.is_substring(sub, index, s)
            if index:
                self.find_sub_string(count+1, sub, index, s, lst)

    def is_substring(self, sub, index, s):
        for i in xrange(index, len(s)-9):
            if sub == s[i:i+10]:
                return i+10
            else:
                pass
        return 0

if __name__ == "__main__":
    str_1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    solution = Solution()
    print solution.findRepeatedDnaSequences(str_1)

# This solution solves the problem, but fails under time limitations.
# Another method need to be explored.