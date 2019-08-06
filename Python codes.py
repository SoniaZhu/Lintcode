## digit is %
## carry is /

## binary question: "2" divide. mid is 0. mid right is 0 1. so size is still 2. avoid

## while loop完如果要用没有loop也能用的variable，需要保持var跳出while和没进loop的状态一样

chr(ord('A'))

#dfs:
    path.append(reminder)
    res.append(path[:])   #copy template
    path.pop()

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
self.queue.empty()

from collections import deque
a = deque()
queue = deque([root])
a.append(1)  # appendleft(1)
a.pop() # popleft()
list(a)   # different from queue.Queue()
len(a)

# list is stack
a = []
a.append(1)
a.pop()
a.insert(index, elem)

a = set() # or {1} but not {}. {} is a dict
a.add(1)
a.remove(1)  # Raises KeyError
a.discard(1)  # if present

from heapq import heappush, heappop
heappush(heap, item)
heappop(heap)
# heappushpop(heap, item)   heapreplace(heap, item)

intervals = sorted(intervals, key = lambda x : x.start)
A.sort()

a = None or a = set() or a = []
if a:

a = ""
print (not a)

current = dummy = ListNode(-1)

''.join(['a','b','c','d'])
s[::-1]
''.join(reversed(s))

## reversed returns iterator. sorted is okay
list(reversed(list))
list.reverse()
list[::-1]

for key in dict:
# py3 its just a view
dict.items()
dict[a] = dict.get(a, 0) + 1   # value if default

a = "ab"
print (a[5:4]=="") # true

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

#swap
nums[index], nums[nextIndex] = nums[nextIndex], nums[index]

# else 1) range not go in 2) range completes w/o break
for i in range(0,0):
    print (1)
    break
else:
    print (2)
## if range not go in, i is not available
## if break, i is intented


C = [[0] * k for i in range(n)]
letter = 'a'    letter * 5 = 'aaaaa'
for d, r in zip(digit, rom):

dict: my_dict.pop('key', None)
my_dict.pop('key')
del myDict['key']
https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
for set, a.remove(1)  # Raises KeyError    a.discard(1)

random.sample(population, k)   # without replacement

# list. comma 分开所有要加到list里的
queue += (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

bfs wiki

int (4.8) = 4   print (8/4) = 2.0
print([[]]*5)  [[],[],[],[],[]]  # but they are all the same (address/refer)
empty_lists = [ [] for i in range(n) ] # better

#content
board[:] = [['XO'[c == 'W'] for c in row] for row in board]
xxx = board[:] #copy

'abc'.index('a')  'abc'.find('a')

# string is not mutable!!!
# cannot add mutable stuff to set or dict
# bfs dx dy don't forget to check boundry <0. and while queue, not visited
