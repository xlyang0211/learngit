class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        count_hash = {}
        lst = []
        for i in xrange(0, len(s)-9):
            if s[i:i+10] in count_hash:
                count_hash[s[i:i+10]] += 1
            else:
                count_hash[s[i:i+10]] = 1
        for item in count_hash:
            if count_hash[item] > 1:
                lst.append(item)
        return lst

if __name__ == "__main__":
    str_1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    solution = Solution()
    print solution.findRepeatedDnaSequences(str_1)