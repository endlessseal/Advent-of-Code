from collections import deque
import time
number_of_elves = 3018458
list_of_elves = deque(list(range(1,number_of_elves+1)))

def solve():
    while True:
        if len(list_of_elves) == 1:
            return list_of_elves[0]
        list_of_elves.rotate(-1)
        list_of_elves.popleft()
x = time.time()
print(solve())
print(time.time()-x)
