__author__ = 'seany'
# Note:
# There are 2 ways to work out this problem:
# 1. get started from the lower 3 bits;
# 2. get started from the higher 3 bits;
# The difference is which way will provide a convenient way to solve the problem.

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit_to_str = {1: 'One',
                            2: 'Two',
                            3: 'Three',
                            4: 'Four',
                            5: 'Five',
                            6: 'Six',
                            7: 'Seven',
                            8: 'Eight',
                            9: 'Nine',
                            10: 'Ten',
                            11: 'Eleven',
                            12: 'Twelve',
                            13: 'Thirteen',
                            14: 'Fourteen',
                            15: 'Fifteen',
                            16: 'Sixteen',
                            17: 'Seventeen',
                            18: 'Eighteen',
                            19: 'Nineteen',
                            20: 'Twenty',
                            30: 'Thirty',
                            40: 'Forty',
                            50: 'Fifty',
                            60: 'Sixty',
                            70: 'Seventy',
                            80: 'Eighty',
                            90: 'Ninety',
                            100: 'Hundred',
                            1000:'Thousand',
                            1000000: 'Billion',
                            1000000000: 'Trillion',
                            }
        str_list = []
        count = 0
        if num == 0:
            return 'Zero'
        divisor = 1000000000
        while num != 0:
            out_str = []
            quotient = num / divisor
            residue = num % divisor
            if quotient:
                q_1 = quotient / 100
                r_1 = quotient % 100
                if q_1:
                    out_str.append(digit_to_str[q_1])
                    out_str.append('Hundred')
                if r_1:
                    q_2 = r_1 / 10
                    r_2 = r_1 % 10
                    if q_2 == 1:
                        out_str.append(digit_to_str[r_1])
                    else:
                        if q_2:
                            out_str.append(digit_to_str[10 * q_2])
                        if r_2:
                            out_str.append(digit_to_str[r_2])
                if count == 0:
                    out_str.append('Billion')
                elif count == 1:
                    out_str.append('Million')
                elif count == 2:
                    out_str.append('Thousand')
            count += 1
            num = residue
            divisor /= 1000
            str_list = str_list + out_str
        return " ".join(str_list).strip()

if __name__ == "__main__":
    solution = Solution()
    print solution.numberToWords(1234567890)




