__author__ = 'seany'

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0:
            return [0]
        original = n * "0"
        my_set = set()
        my_set.add(original)
        my_list = [original]
        x = n - 1
        while len(my_set) != 2 ** n:
            new_code = self.change_a_bit(x, original)
            if new_code not in my_set:
                my_set.add(new_code)
                my_list.append(new_code)
                original = new_code
                x = n - 1
            else:
                if x > 0:
                    x -= 1
        return [int(i, 2) for i in my_list]

    def change_a_bit(self, x, original):
        if original[x] == "0":
            if x != len(original) - 1:
                original = original[:x] + "1" + original[x+1:]
            else:
                original = original[:x] + "1"
        else:
            if x != len(original) - 1:
                original = original[:x] + "0" + original[x+1:]
            else:
                original = original[:x] + "0"
        return original

if __name__ == "__main__":
    solution = Solution()
    print solution.grayCode(0)

# Please take notice of x in the algorithm, because leetcode cannot recognise the value sequence such as when n = 2:
# sequence [0, 1, 3, 2] will be OK, but [0, 2, 3, 1] will be wrong, which is actually another right answer;