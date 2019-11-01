# Listnode.next: always check null
## digit is %
## carry is /

## binary question: "2" divide. mid is 0. mid right is 0 1. so size is still 2. avoid

## while loop完如果要用没有loop也能用的variable，需要保持var跳出while和没进loop的状态一样

## int(x) str(x)
isupper(), islower(), lower(), upper()

a = dict()
a.get(1) -> None    a[1] -> KeyError

s.index('@')  find (-1)
local_name, domain_name = email.split("@")
chr(ord('A'))
txt = "I like bananas"
x = txt.replace("bananas", "apples")

#dfs:
    path.append(reminder)
    res.append(path[:])   #copy template
    path.pop()

sys.maxint # py2
sys.maxsize # py3
float("-inf") # always work. large

sum = -1 if nums[i] == 0 else 1

abbr[j].isdigit()
a.isalpha()
startswith("xx")
isalnum()
hexa = int(s, base=16)

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
## extend()  extendleft()

# list is stack
a = []
a.append(1)
a.extend(list)
a.pop()
a.insert(index, elem)

a = set() # or {1} but not {}. {} is a dict
a.add(1)
a.remove(1)  # Raises KeyError
a.discard(1)  # if present

# min heap   [1,2]
from heapq import heappush, heappop
heappush(heap, item)
heappop(heap)
# heap[0] min
# heappushpop(heap, item)  always min  heapreplace(heap, item)  the min will always out

# lambda
intervals = sorted(intervals, key = lambda x : x.start)
l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
def abc(x):
    y,z = x.split(" ")[1:],x.split(" ")[0]
    y.append(z)
    return y
ll = sorted(ll, key = abc)

max(num, key=sumDigit)  max(num, num1, num2, key=len)
A.sort()

a = None or a = set() or a = []
if a:

a = ""
print (not a)

current = dummy = ListNode(-1)

''.join(['a','b','c','d'])
s[::-1]   # return new
''.join(reversed(s))

## reversed returns iterator. sorted is okay. print
list(reversed(list))
list.reverse()
list[::-1]

for key in dict:
# py3 its just a view
for key, value in d.items():
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
# for d, r in zip(digit, rom):
for i, j in zip('ABCD', 'xy'):
  print (i, j)
# A x, B y

dict: my_dict.pop('key', None)
my_dict.pop('key')
del myDict['key']
https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
for set, a.remove(1)  # Raises KeyError    a.discard(1)
# lists
# del pop index. remove value.
# dictionary
# del pop key.


import random
random.sample(population, k)   # without replacement
random.randint(0, 10)  #[0, 10]

# list. comma 分开所有要加到list里的
queue += (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

bfs wiki

int (4.8) = 4   print (8/4) = 2.0
print([[]]*5)  [[],[],[],[],[]]  # but they are all the same (address/refer)
empty_lists = [ [] for i in range(n) ] # better

#content
board[:] = [['XO'[c == 'W'] for c in row] for row in board]  # content changed as board is parameter
xxx = board[:] #copy

'abc'.index('a') exception 'abc'.find('a')  -1

# string is not mutable!!!
# cannot add mutable stuff to set or dict. tuple is not mutable but list is
# bfs dx dy don't forget to check boundry <0. and while queue, not visited

# iterable (list, tuple, set, dictionary...)
1 in (1,2,3) or 1 in [1,2,3]

#python floor division:  3//-2 = -2
int(3.2) = 3    int(-3.2) = -3   # int(3/-2) to get 3/-2 in java

# split at any space
data.split()
' '.join(bfs_order)

for v in vs:  ## dynamic
for i in range(len(vs)) ## static

# You cannot use a list as a key because a list is mutable. ... (You can only
# use a tuple as a key if all of its elements are immutable.)

object() 空对象
用 xxx is not None instead of not xxx (b/c 0 or None?)

method(lst) -> lst[1]=1 or lst.remove() both works

for new_s in (s[:i]+'--'+s[i+2:] for i in range(len(s)-1) if s[i:i+2]=='++'):

for i in range(0):
  print('a')
else:
  print('b')
# no print(i)
# but b

# string format
f"{to_lowercase(name)} is funny."
ap = collections.defaultdict(list)


def calculateSquare(n):
  return n*n
numbers = (1, 2, 3, 4)
result = map(lambda x: 1 if 'e' in x else 0, numbers)
result = map(calculateSquare, numbers)
numbersSquare = set(result)
