class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        has_find = {}
        not_find = {}
        l_s = len(s)
        l_t = len(t)
        begin = 0
        end = 0
        MIN = l_s + 1
        count = 0
        if l_t == 0:
            return ""
        if l_s < l_t:
            return ""
        for i in xrange(l_t):
            if t[i] in not_find:
                not_find[t[i]] += 1
            else:
                not_find[t[i]] = 1
        for i in xrange(l_s):
            if s[i] not in not_find:
                has_find[s[i]] = 0
            else:  # The character is in t;
                print "The key is:", s[i]
                if s[i] not in has_find:
                    has_find[s[i]] = 1
                else:
                    has_find[s[i]] += 1
                if has_find[s[i]] <= not_find[s[i]]:
                    count += 1
                if count == l_t:  # find a scope where the t exists;
                    while begin < i:
                        if s[begin] not in not_find:
                            begin += 1
                        if has_find[s[begin]] > not_find[s[begin]]:
                            begin += 1
                        else:
                            break
                    if i - begin + 1 < MIN:
                        MIN = i - begin + 1
                        end = i
        return s[begin: end+1]

if __name__ == "__main__":
    solution = Solution()
    S = "adefbca"
    T = "abc"
    print solution.minWindow(S, T)
