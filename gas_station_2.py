class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) != len(cost):
            return None
        else:
            number_of_station = len(gas)
            net_residue = []
            for station_index in xrange(number_of_station):
                net_residue.append(gas[station_index] - cost[station_index])
            # This binary division for searching the start index is not correct:
            # for example. gas = [1, 2, 3, 3] and cost = [2, 1, 5, 1]
            # This method will get 1 as the start index and finally find it wrong
            # But actually the right answer is 3;
            start_index = self.middle(net_residue, 0, number_of_station-1)
            net_residue = net_residue[start_index:] + net_residue[:start_index]
            net_accumulation = 0
            for i in net_residue:
                net_accumulation += i
                if net_accumulation < 0:
                    return -1
            return start_index

    def middle(self, list, first, last):
        if first != last:
            middle = (first + last)/2
            print "The middle is:", middle
            if self.sum_up(list, first, middle) >= 0:
                return self.middle(list, first, middle)
            else:
                return self.middle(list, middle+1, last)
        else:
            return first

    def sum_up(self, list, first, last):
        sum = 0
        for i in xrange(first, last+1):
            sum += list[i]
        return sum


if __name__ == "__main__":
    gas = [1, 2, 3, 3]
    cost = [2, 1, 5, 1]
    #gas = [4]
    #cost = [5]
    solution = Solution()
    print solution.canCompleteCircuit(gas, cost)