class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        digit_to_char = {"1": [],
                        "2": ["a", "b", "c"],
                        "3": ["d", "e", "f"],
                        "4": ["g", "h", "i"],
                        "5": ["j", "k", "l"],
                        "6": ["m", "n", "o"],
                        "7": ["p", "q", "r", "s"],
                        "8": ["t", "u", "v"],
                        "9": ["w", "x", "y", "z"],
                        "0": []
        }
        my_str = ""
        my_str_list = []
        self.recursive_generation(my_str, my_str_list, digit_to_char, digits)
        return my_str_list

    def recursive_generation(self, my_str, my_str_list, digit_to_char, digits):
        print "en"
        if len(digits) == 0:
            my_str_list.append(my_str)
        else:
            for char in digit_to_char[digits[0]]:
                my_str_new = my_str + char
                print my_str_new
                self.recursive_generation(my_str_new, my_str_list, digit_to_char, digits[1:])

if __name__ == "__main__":
    solution = Solution()
    print solution.letterCombinations("234")

