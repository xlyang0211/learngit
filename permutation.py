class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        tmp = []
        self.permutation(num, result, tmp)
        return result
    def permutation(self, list, result, tmp):
        if len(list) == 1:
            tmp.append(list[0])
            print "tmp is:", tmp
            if tmp not in result:
                result.append(tmp)
        else:
            for i in xrange(len(list)):
                tmp_tmp = tmp[:]
                tmp_tmp.append(list[i])
                list_tmp = list[:]
                del list_tmp[i]
                self.permutation(list_tmp, result, tmp_tmp)
                tmp_tmp = tmp

if __name__ == "__main__":
    solution = Solution()
    list = [1]
    result = []
    tmp = []
    print solution.permutation(list, result, tmp)
    print result
    print len(result)