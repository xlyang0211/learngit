class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        hash_char = {}
        count = 0  # keep the length of non-repeating sub-str
        longest = 0  # keep the length of longest non-repeating sub-str
        start = 0  # keep the start index of current non-repeating sub-str
        for index, char in enumerate(s):
            if char not in hash_char or hash_char[char] < start:
                hash_char[char] = index
                if index == len(s)-1:  # deal with the situation when the string reaches its end
                    if longest < (index - start + 1):
                        return index - start + 1
                    else:
                        pass
            else:
                if start == 0:  # the first non-repeating sub-str
                    count = index - start
                    start = hash_char[char] + 1
                else:
                    count = index - start
                    start = hash_char[char] + 1
                hash_char[char] = index
                if count > longest:
                    longest = count
                else:
                    pass
        return longest

if __name__ == "__main__":
    str = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
    str_1 = "abbac"
    solution = Solution()
    print solution.lengthOfLongestSubstring(str)
