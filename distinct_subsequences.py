__author__ = 'seany'
import time
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        s_count = 0
        t_count = 0
        return self.num_distinct(S, T, s_count, t_count)

    def num_distinct(self, S, T, s_count, t_count):
        sum = 0
        for i in xrange(len(S[s_count:])):
            # This if branch is used to pruning, but actually the time seems to consume more;
            if len(S) - s_count - i < len(T) - t_count:
                return sum
            elif S[s_count+i] == T[t_count]:
                if t_count == len(T) - 1:
                    sum += 1
                else:
                    sum += self.num_distinct(S, T, s_count+i+1, t_count+1)
        return sum

if __name__ == "__main__":
    S = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    T = "bddabdcae"
    solution = Solution()
    a = time.clock()
    print solution.numDistinct(S, T)
    b = time.clock()
    print b - a

# The problem is solved with DFS, but actually many intermittent data are calculated repreatedly;
# So the method of dynamic programming is introduced to eliminate the repetition by setting up a record table;