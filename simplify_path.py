__author__ = 'seany'
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        path_list = path.split("/")
        new_path_list = []
        for i in xrange(len(path_list)):
            if path_list[i] == "." or path_list[i] == "":
                pass
            elif path_list[i] == "..":
                new_path_list = new_path_list[:-1]
            else:
                new_path_list.append(path_list[i])
        return "/" + "/".join(new_path_list)

if __name__ == "__main__":
    solution = Solution()
    path = "/home/usr/../../home"
    print solution.simplifyPath(path)