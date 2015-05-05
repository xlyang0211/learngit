class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        hash_s = {}
        # Construct hash for s;
        for i in xrange(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = list(i)
            else:
                hash_s[s[i]].append(i)

