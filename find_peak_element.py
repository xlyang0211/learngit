class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        length = len(num)
        if length == 0:
            return None
        elif length == 1:
            return 0
        i = length / 2
        if i == 0:
            if num[i] > num[i+1]:
                return i
            else:
                pass
            return self.findPeakElement(num[1:]) + 1
        elif i == length - 1:
            if num[i] > num[i-1]:
                return i
            else:
                pass
            return self.findPeakElement(num[:i])
        else:
            if num[i] > num[i-1] and num[i] > num[i+1]:
                return i
            else:
                if num[i] <= num[i-1]: # This step is very important, unless the boundary is very hard to deal with;
                    return (self.findPeakElement(num[:i+1]))
                elif num[i] <= num[i+1]:
                    return (self.findPeakElement(num[i:])+i)

if __name__ == "__main__":
    num = [3, 2, 1]
    solution = Solution()
    print solution.findPeakElement(num)