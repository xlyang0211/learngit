class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        quotient = 0
        sign = 1
        if dividend > 0:
            if divisor > 0:
                sign = 1
            elif divisor == 0:
                return MAX_INT
            else:
                sign = 0
                divisor = -divisor
        elif dividend == 0:
            if divisor == 0:
                return MAX_INT
            else:
                return 0
        else:
            if divisor > 0:
                sign = 0
                dividend = -dividend
            elif divisor == 0:
                return MAX_INT
            else:
                sign = 1
                dividend = -dividend
                divisor = -divisor
        while dividend > divisor:
            dividend = dividend - divisor
            quotient += 1
        return quotient