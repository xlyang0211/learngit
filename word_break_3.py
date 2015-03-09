class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        flag_list = [False] * (len(s)+1) # add one element to mark the position right after the last position;
        flag_list[0] = True
        for i in xrange(len(s)):
            if flag_list[i]:
                for word in dict:
                    if self.string_start_with_sub(s[i:], word):
                        flag_list[i+len(word)] = True
                    else:
                        continue
            else:
                continue
        return flag_list[-1]

    def string_start_with_sub(self, s, sub):
        """
        :param s: The string to judge if contain the sub;
        :param sub: The sub string to judge if in the string;
        :return: True or False;
        """
        for i in xrange(len(s)):
            if s[:i+1] == sub:
                return True
        return False

solution = Solution()
s = "bacccc"
dict = ["ac", "b", "c", "bbbb", "bbb", "bbbb"]
print solution.wordBreak(s, dict)

# The most important and difficult part of the flag_list, one more bit is in need to start or end the mark, there are
# two scheme to choose from:
# 1. flag_list[0] is initialized as true, as a start, and every other true bit mark the end index of word in dict accu-
#    mulatively.
# 2. flag_list[0] is initialized as true, as the start of a word index, so does every true in the list;