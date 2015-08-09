class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) != len(cost):
            return False
        else:
            num_of_station = len(gas)
            for start_index in xrange(num_of_station):
                gas_new = gas[start_index:] + gas[:start_index]
                cost_new = cost[start_index:] + cost[:start_index]
                gas_accumulation = 0
                cost_accumulation = 0
                completion_mark = 1
                for station_index in xrange(num_of_station):
                    gas_accumulation += gas_new[station_index]
                    cost_accumulation += cost_new[station_index]
                    if gas_accumulation >= cost_accumulation:
                        pass
                    else:
                        completion_mark = 0
                        break
                if completion_mark == 1:
                    return start_index
                else:
                    pass
            return -1

if __name__ == "__main__":
    gas = [1, 2]
    cost = [2, 1]
    solution = Solution()
    print solution.canCompleteCircuit(gas, cost)