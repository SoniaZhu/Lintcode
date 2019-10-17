class Solution:
    """
    @param paths: a list of string
    @return: all the groups of duplicate files in the file system in terms of their paths
    """
    def findDuplicate(self, paths):
        # Write your code here
        map = collections.defaultdict(list)
        for path in paths:
            root, *files = path.split(" ")
            for file in files:
                filename, content = file.split("(")
                map[content[:-1]].append(root + "/" + filename)
        return [map[k] for k in map if len(map[k]) > 1]
