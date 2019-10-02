# 怎么判断是不是一棵树 (3个条件满足2个即可)
# 1 边 一定要等于 n-1 (union find, BFS)
#
# 2 从0 节点一定可以连通到其他所有节点。 (BFS)
#
# 3 所有节点不成环（union Find)

## solves problem 1. hash[node] maybe null (keyerror) 2. circle edges len = n - 1
## complexity https://segmentfault.com/a/1190000005687618
from collections import deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        hash = dict()
        for i in range(n):
            hash[i] = set()
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            hash[n1].add(n2)
            hash[n2].add(n1)

        if n <= 0:
            return False
        if len(edges) != n - 1:
            return False

        queue = deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            for child in hash[node]:
                if child in visited:
                    continue
                visited.add(child)
                queue.append(child)
        return len(visited) == n

## first try. beat 33%
# struggle: 1. hash save undirected edge. (if direct, not know visit order). 1->2->1 valid
# 2. valid tree: no circle. no isolated.
from collections import deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        hash = dict()
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            if n1 not in hash:
                hash[n1] = set()
            hash[n1].add(n2)
            if n2 not in hash:
                hash[n2] = set()
            hash[n2].add(n1)

        if n <= 0:
            return True
        queue = deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            if node not in hash:
                continue
            children = hash[node]
            for child in children:
                if child in visited:
                    return False
                visited.add(child)
                queue.append(child)
                hash[child].remove(node)
        return len(visited) == n

## union find. did not read.
## java code https://www.jiuzhang.com/solution/graph-valid-tree/#tag-highlight-lang-java
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False

        self.father = {i: i for i in range(n)}
        self.size = n

        for a, b in edges:
            self.union(a, b)

        return self.size == 1

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
