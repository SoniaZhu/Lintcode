## digit is %
## carry is /

## binary question: "2" divide. mid is 0. mid right is 0 1. so size is still 2. avoid

## while loop完如果要用没有loop也能用的variable，需要保持var跳出while和没进loop的状态一样

chr(ord('A'))

sys.maxint # py2
sys.maxsize # py3
float("inf") # always work. large

sum = -1 if nums[i] == 0 else 1

abbr[j].isdigit()
a.isalpha()

max([1, 2, 3])

s.strip()  #s.lstrip()  s.rstrip()

from Queue import Queue  # py2
from queue import Queue  # py3
self.queue = Queue()
self.queue.get()
self.queue.put(val)
self.queue.qsize()

from collections import deque
a = deque()
a.append(1)  # appendleft(1)
a.pop() # popleft()
list(a)   # different from queue.Queue()
len(a)

# list is stack
a = []
a.append(1)
a.pop()

a = set() # or {1} but not {}. {} is a dict
a.add(1)
a.remove(1)  # Raises KeyError
a.discard(1)  # if present

from heapq import heappush, heappop
heappush(heap, item)
heappop(heap)
# heappushpop(heap, item)   heapreplace(heap, item)

## %

intervals = sorted(intervals, key = lambda x : x.start)
A.sort()

a = None
if a:

a = ""
print (not a)

current = dummy = ListNode(-1)

''.join(['a','b','c','d'])
s[::-1]
''.join(reversed(s))

list(reversed(list))
list.reverse()
list[::-1]

for key in dict:
# py3 its just a view
dict.items()

a = "ab"
print (a[5:4]=="") #true

5 // 2


######
A = {}
class Solution:
    B = {}
    def xx(self):
        self.C = {}
    def xxx(self):
        A
        self.B
        self.C
