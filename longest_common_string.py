# Analysis: The first step is to draw the shortest string in string list;
# And the computational complexity is O(mn), is there a more compact algorithm?
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        # First find the least-length of the list of strings:
        least_length = len(strs[0])
        for str in strs:
            if len(str) < least_length:
                least_length = len(str)
            else:
                pass
        if least_length == 0:
            return ""
        first_str = strs[0]
        common_prefix_index = 0
        flag = 0
        for i in xrange(least_length):
            for str in strs[1:]:
                if str[i] == first_str[i]:
                    pass
                else:
                    flag = 1
            if flag == 1:
                common_prefix_index = i
                break
        print i
        print flag
        if flag: # exit the loop with break
            return first_str[:i]
        else: # exit the loop normally.
            return first_str[:i+1]


if __name__ == "__main__":
    strs = ["hello", "helha", "heldo"]
    st = ["a", "ab"]
    solution = Solution()
    print solution.longestCommonPrefix(strs)

