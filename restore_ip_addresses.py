# Valid ip addresses should be:
# 1. divide into four part;
# 2. every part should be between 0~255
class Solution:
    def restore_ip_addresses(self, s):
        """
        Given a string containing digits, return all valid ip addresses;
        :param s: string of digits;
        :return: list of valid ip addresses;
        """
        ip = ""
        result = []
        self.dfs(s, 0, ip, result)
        return result

    def dfs(self, s, step, ip, result):
        """
        Using dfs to generate all valid ip addresses
        """
        if len(s) > (4-step)*3:
            return
        elif len(s) < 4-step:
            return
        else:
            if step == 3:
                if 10 <= int(s) <= 255 and int(s[0]):
                    ip = ip + "." + s
                    result.append(ip)
                elif 0<= int(s) < 10 and len(s) == 1:
                    ip = ip + "." + s
                    result.append(ip)
            else:
                if step != 0:
                    ip += "."
                self.dfs(s[1:], step+1, ip + s[:1], result)
                if int(s[0]) != 0:
                    self.dfs(s[2:], step+1, ip + s[:2], result)
                if 0<= int(s[:3]) <= 255 and int(s[0]) != 0:
                    self.dfs(s[3:], step+1, ip + s[:3], result)

if __name__ == "__main__":
    s = "010010"
    solution = Solution()
    print solution.restore_ip_addresses(s)