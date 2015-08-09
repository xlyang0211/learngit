__author__ = 'xlyang0211'


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses <= 1:
            return True
        # construct adjacent list;
        adjacent_hash = {}
        for i in prerequisites:
            if i[0] not in adjacent_hash:
                adjacent_hash[i[0]] = []
            adjacent_hash[i[0]].append(i[1])

        # Then judge if there is circle in the graph
        for i in xrange(numCourses):
            if i not in adjacent_hash:
                pass
            else:
                timer_list = [0] * numCourses
                if self.dfs(i, timer_list, adjacent_hash, 1):  # there is circle in the graph;
                    return False
        return True

    def dfs(self, i, timer_list, adjacent_hash, count):
        if i not in adjacent_hash:
            return False
        else:
            for j in adjacent_hash[i]:
                if timer_list[i] >= timer_list[j] and timer_list[j] != 0:
                    return True
                else:
                    count += 1
                    timer_list[j] = count
                    if self.dfs(j, timer_list, adjacent_hash, count):
                        return True
            return False

if __name__ == "__main__":
    solution = Solution()
    numCourse = 4
    course_list = [[1, 2], [2, 0], [0, 3]]
    print solution.canFinish(numCourse, course_list)

# This method works, but time exceeds.
