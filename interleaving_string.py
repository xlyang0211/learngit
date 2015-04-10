__author__ = 'seany'
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        return self.is_interleave(s1, s2, s3, 0, 0, 0)

    def is_interleave(self, s1, s2, s3, index_1, index_2, index_3):
        print "\n"
        print "index 1:", index_1
        print "index 2:", index_2
        print "index 3:", index_3
        rem_1 = len(s1) - index_1
        rem_2 = len(s2) - index_2
        rem_3 = len(s3) - index_3
        if rem_1 + rem_2 < rem_3:
            return False
        elif rem_1 == 1 and rem_3 == 1:
            if s1[index_1] == s3[index_3]:
                return True
            else:
                return False
        elif rem_2 == 1 and rem_3 == 1:
            if s2[index_2] == s3[index_3]:
                return True
            else:
                return False
        else:
            try:
                result_1 = False
                result_2 = False
                if s1[index_1] == s3[index_3]:
                    result_1 = self.is_interleave(s1, s2, s3, index_1+1, index_2, index_3+1)
                if s2[index_2] == s3[index_3]:
                    result_2 = self.is_interleave(s1, s2, s3, index_1, index_2+1, index_3+1)
                return result_1 or result_2
            except:
                return False

if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s4 = "aadbbbaccc"
    solution = Solution()
    print solution.isInterleave(s1, s2, s4)