class Solution:
    # @return an integer
    def reverse(self, x):
        div = abs(x)
        res = 0
        reverse_string = ""
        head_zero_flag = 0
        while div >= 10:
            res = div % 10
            div /= 10
            if res == 0:
                if head_zero_flag == 0:
                    pass
                else:
                    reverse_string += str(res)
                    head_zero_flag = 1
            else:
                reverse_string += str(res)
                head_zero_flag = 1
        reverse_string += str(div)
        print "The reverse_string is:", reverse_string
        if int(reverse_string) > 2**31:
            print "The number exceeds the range."
            return 0
        else:
            if x < 0:
                return (0 - int(reverse_string))
            else:
                return int(reverse_string)

if __name__ == "__main__":
    solution = Solution()
    print solution.reverse(1000000003)


