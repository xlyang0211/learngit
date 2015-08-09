class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_num = dict()
        index_1 = 0
        index_2 = 0
        for indexCurrent, number in enumerate(num):
            hash_num[number] = indexCurrent
        count = 0
        for number in num:
            diff = target - number
            if diff in hash_num.keys():
                index_1 = count
                index_2 = hash_num.get(diff)
                if index_1 != index_2:
                    break
            count = count + 1
        return (index_1+1, index_2+1)

if __name__ == "__main__":
    num = [2, 5, 6, 7, 9]
    solution = Solution()
    print solution.twoSum(num, 7)
