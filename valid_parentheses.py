class Solution:
    # @return a boolean
    def isValid(self, s):
        s_new = ""
        pair_flag = 0
        if len(s) == 0:
            return True
        for c in s:
            if len(s_new) == 0:
                s_new = s_new + c
                pair_flag += 1
                pass
            elif (s_new[-1] == "(" and c == ")") or \
                 (s_new[-1] == "[" and c == "]") or \
                 (s_new[-1] == "{" and c == "}"):
                s_new = s_new[:-1]
                pair_flag -= 1
            else:
                s_new = s_new + c
                pair_flag += 1
        if pair_flag:
            return False
        else:
            return True
