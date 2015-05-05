class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    # This algorithm can generated the right result but manages a bad time complexity. Please see version 2;
    def multiply(self, num1, num2):
        zero_fill_count = 0
        result = ""
        for char_2 in reversed(num2):
            tmp = ""
            carry = "0"
            for char_1 in reversed(num1):
                (sum, carry) = self.char_multiply(char_1, char_2, carry)
                tmp = sum + tmp
            tmp = tmp + "0"*zero_fill_count
            if carry != "0":
                tmp = carry + tmp
            zero_fill_count += 1
            result = self.string_addition(result, tmp)
        return result

    def char_multiply(self, char_1, char_2, carry):
        int_1 = int(char_1)
        int_2 = int(char_2)
        carry = int(carry)
        sum = (int_1 * int_2 + carry) % 10
        carry = (int_1 * int_2 + carry) / 10
        return (str(sum), str(carry))

    def char_addition(self, char_1, char_2, carry):
        int_1 = int(char_1)
        int_2 = int(char_2)
        carry_1 = carry
        carry = int(carry)
        sum = (int_1 + int_2 + carry) % 10
        carry = (int_1 + int_2 + carry) / 10
        return (str(sum), str(carry))

    def string_addition(self, str_1, str_2):
        digit = max(len(str_1), len(str_2))
        result = ""
        carry = "0"
        for i in xrange(1, digit+1):
            char_1 = "0"
            char_2 = "0"
            sum = "0"
            if i > len(str_1):
                char_1 = "0"
            else:
                char_1 = str_1[-i]
            if i > len(str_2):
                char_2 = "0"
            else:
                char_2 = str_2[-i]
            (sum, carry) = self.char_addition(char_1, char_2, carry)
            result = sum + result
        return result

if __name__ == "__main__":
    solution = Solution()
    str_1 = "2"
    str_2 = "4"
    print solution.multiply(str_1, str_2)
