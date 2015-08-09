class Solution:
    # @return a string
    def convertToTitle(self, num):
        str = ""
        while num > 26:
            rem = num % 26
            num = num / 26
            if rem == 0:
                str =  "Z" + str
                num = num - 1
            else:
                str = chr(rem + 64) + str
        str = chr(num + 64) + str
        return str

if __name__ == "__main__":
    solution = Solution()
    print solution.convertToTitle(51)
