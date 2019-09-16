## see data stream
## first time see: add. second time: delete. third time: do nothing

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        map = dict()
        for c in str:
            map[c] = map.get(c, 0) + 1
        for c in map:
            if map[c] == 1:
                return c

## data stream
class Node:
    def __init__(self, char, next=None):
        self.char = char
        self.next = next

class DataStream:
    def __init__(self, dupChars=set(), charToPrevNode=dict()):
        self.dupChars = dupChars
        self.charToPrevNode = charToPrevNode
        self.dummy = Node('.')
        self.tail = self.dummy

    def add(self, char):
        if char in self.dupChars:
            return
        if char not in self.charToPrevNode:
            node = Node(char)
            self.charToPrevNode[char] = self.tail
            self.tail.next = node
            self.tail = node
            return
        self.dupChars.add(char)
        prevNode = self.charToPrevNode[char]
        prevNode.next = prevNode.next.next
        self.charToPrevNode.pop(char)
        if prevNode.next is None:
            self.tail = prevNode
        else:
            self.charToPrevNode[prevNode.next.char] = prevNode
    def firstUniqueChar(self):
        return self.dummy.next.char

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        ds = DataStream()
        for c in str:
            ds.add(c)
        return ds.firstUniqueChar()
