from collections import deque

number_of_elves = 3018458
list_of_elves = deque(list(range(1,number_of_elves+1)))

def solve():
    list_of_elves.rotate((len(list_of_elves)+1)//2)
    while True:
        if len(list_of_elves) == 1:
            return list_of_elves.pop()
        list_of_elves.popleft()
        list_of_elves.rotate((((len(list_of_elves)+1)//2)*2) - 1)

print(solve())

