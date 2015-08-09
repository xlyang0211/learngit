class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        length = 0
        if len(a) >= len(b):
            length = len(a)
        else:
            length = len(b)
            a, b = b, a
        carry = "0"
        sum = ""
        a = list(a)
        a.reverse()
        b = list(b)
        b.reverse()
        for i in xrange(length):
            if i > len(b) - 1:
                print "carry is:", carry
                print "a[i] is:", a[i]
                if a[i] == "0" and carry == "0":
                    sum = "0" + sum
                    carry = "0"
                elif a[i] == "1" and carry == "1":
                    sum = "0" + sum
                    carry = "1"
                else:
                    sum = "1" + sum
                    carry = "0"
                    print "sum is:", sum
            else:
                print "a[i]:", a[i]
                print "b[i]:", b[i]
                print "carry:", carry
                if a[i] == "0" and b[i] == "0":
                    if carry == "0":
                        sum = "0" + sum
                        carry = "0"
                    else:
                        sum = "1" + sum
                        carry = "0"
                elif a[i] == "0" and b[i] == "1":
                    if carry == "0":
                        sum = "1" + sum
                        carry = "0"
                    else:
                        sum = "0" + sum
                        carry = "1"
                if a[i] == "1" and b[i] == "0":
                    if carry == "0":
                        sum = "1" + sum
                        carry = "0"
                    else:
                        sum = "0" + sum
                        carry = "1"
                if a[i] == "1" and b[i] == "1":
                    if carry == "0":
                        sum = "0" + sum
                        carry = "1"
                    else:
                        sum = "1" + sum
                        carry = "1"

        if carry == "1":
            sum = "1" + sum
        else:
            pass
        return sum

if __name__ == "__main__":
    a = "100"
    b = "110010"
    solution = Solution()
    print solution.addBinary(a, b)