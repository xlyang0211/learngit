class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # Build the graph: using adjacent table (or you can use adjacent matrix)
        new_dict = dict[:]
        new_dict.append(start)
        new_dict.append(end)
        adjacent_table = self.build_undirected_graph(new_dict)
        print adjacent_table
        # Find the path length from start to the end
        unvisited = dict[:]  # None represent the distance, use unvisited to record those unvisited nodes;
        unvisited.append(start)
        unvisited.append(end)
        result = {x: None for x in dict} # Use result to record the distance info. result won't be deleted;
        result[start] = 1
        result[end] = None
        visited = {}  # currently visited is empty
        while True:  # or you can use while unvisited is not empty;
            if not unvisited:
                break
            min_key = self.extract_min(unvisited, result)
            unvisited.remove(min_key)
            for adjacent in adjacent_table[min_key]: # undirected graph, this may cause back trace;
                if adjacent in unvisited:  # Prevent back trace, i.e., you've done a to b, no need b to a;
                    result[adjacent] = result[min_key] + 1
        return result

    def extract_min(self, unvisited, result):
        """
        maintain a heap, unvisited records the node unvisited, and result records the distance info;
        :param unvisited:
        :param result:
        :return: The minimum node;
        """
        min_value = None
        min_item = None
        for item in unvisited:
            if result[item] == None:
                pass
            elif min_value == None:
                min_item = item
            elif result[item] < min_value:
                min_item = item
        return min_item

    def build_undirected_graph(self, dict):
        """
        The graph is stored in a dictionary.
        :param dict: The dict is a list of word
        :return: return a real dictionary of the graph
        """
        adjacent_table = {}
        for item_1 in dict:
            adjacent_table[item_1] = []
            for item_2 in dict:
                if item_1 == item_2:
                    continue
                else:
                    if self.judge_connection(item_1, item_2):
                        adjacent_table[item_1].append(item_2)
        return adjacent_table

    def judge_connection(self, str_1, str_2):
        """
        To judge if 2 string are adjacent, like 'dog' and 'cog';
        :param str_1:
        :param str_2:
        :return:
        """
        length_1 = len(str_1)
        length_2 = len(str_2)
        if length_1 != length_2:
            return False
        else:
            count = 0
            for i in xrange(length_1):
                if str_1[i] != str_2[i]:
                    count += 1
            if count != 1:
                return False
            else:
                return True

if __name__ == "__main__":
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
    solution = Solution()
    print solution.build_undirected_graph(dict)
    print solution.ladderLength(start, end, dict)