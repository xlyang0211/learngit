class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # first step: build the graph
        graph = {start: [],
                 end: [],
                 item: [],
                 ...
        }
        result = {start: 0,
                  end: x,
                  item: x,
                  ...
        }
        # Second, how to implement BFS to extract the shortest path?
        while True:
            count = 0
            get item in minimum graph value:
                for every adjacent item of the minimum value:
                    their value = minimum value + 1
            count += 1
            delete the minimum item in result  # So that two results are needed.
            if count == len(dict) + 2:
                break  # only need to try every node to finish search
