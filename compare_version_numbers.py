class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        num1 = ""
        num2 = ""
        if "." in version1:
            index_1 = version1.index(".")
            num1 = version1[:index_1]
            version1 = version1[index_1+1:]
        else:
            num1 = version1
            version1 = ""
        if "." in version2:
            index_2 = version2.index(".")
            num2 = version2[:index_2]
            version2 = version2[index_2+1:]
        else:
            num2 = version2
            version2 = ""
        print num1
        print num2
        if num1 == "" or num2 == "":
            if num1 == "" and num2 == "":
                return 0
            elif num1 == "":
                num1 = "0"
            else:
                num2 = "0"
        if int(num1) < int(num2):
            return -1
        elif int(num1) > int(num2):
            return 1
        elif int(num1) == int(num2) and version1 == "" and version2 == "":
            return 0
        else:
            return self.compareVersion(version1, version2)

if __name__ == "__main__":
    solution = Solution()
    print solution.compareVersion("2.1.2", "2.1.2.0.1")