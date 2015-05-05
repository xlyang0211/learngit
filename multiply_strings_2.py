class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if len(num1) == len(num2) == 1:
            return self.char_multiply(num1, num2, "0")
        else:
            if len(num1) >= len(num2):
                pass
            else:
                num1, num2 = num2, num1
            sub_num_1 = num1[:len(num1)/2]
            sub_num_2 = num1[len(num1)/2:]
            result_1 = self.multiply(sub_num_1, num2) + "0"*len(sub_num_2)
            result_2 = self.multiply(sub_num_2, num2)
            result = self.string_addition(result_1, result_2)
            return result

    def char_multiply(self, char_1, char_2, carry):
        int_1 = int(char_1)
        int_2 = int(char_2)
        carry = int(carry)
        return str(int_1 * int_2 + carry)

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
        if carry != "0":
            return carry + result
        else:
            return result

if __name__ == "__main__":
    solution = Solution()
    str_1 = "2476489356"
    str_2 = "8952587852548754785"
    print solution.multiply(str_1, str_2)
