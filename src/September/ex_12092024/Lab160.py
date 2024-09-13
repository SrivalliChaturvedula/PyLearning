# Collections in Python
# Basic data structures - list, tuple, set and dictionary
# Advanced - deque: Queue, defaultDict, counter, orderedDict, chainMap, nameTuple

# deque - double ended queue - FirstInFirstOut like bus stand queue or airport queue

# A list- like sequence optimized for data accesses near its endpoints.

from collections import deque

# create a deque
d = deque()  # we can create deque with no elements this way
d2 = deque([1, 2, 3])
# we can create deque with elements in the above way
print(d2)

d2.append(4)
print(d2)

# append values to the left: it will only add one single element
d2.appendleft(5)
print(d2)

# extend to the right: extend can add list of items
d2.extend([5, 6, 7])
print(d2)

# to remove first and last elements from the deque
print(d2.pop())
print(d2.popleft())
print(d2)

output = d2.reverse()
print(d2)

d.insert(0, "ram")
d.insert(1,"Valli")
print(d)








