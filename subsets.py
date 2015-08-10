__author__ = 'seany'

    def combine(self, n, k):
        tmp_list = []
        ret = []
        self.bfs(n, k, 0, tmp_list, ret)
        return ret

    def bfs(self, n, k, index, tmp_list, ret):
        # print n, k, index, tmp_list, ret
        if len(tmp_list) == k:
            ret.append(tmp_list)
        elif n - index < k - len(tmp_list):
            pass
        else:
            for i in xrange(index, n - (k - len(tmp_list)) + 1):
                self.bfs(n, k, i+1, tmp_list+[i+1], ret)


# This algorithm can take use of the realization of combinations.