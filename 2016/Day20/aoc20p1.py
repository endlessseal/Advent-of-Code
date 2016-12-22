
def construct_list():
    list_of_ranges = []
    with open('aoc20.txt', 'r') as fp:
        for each_line in fp.read().splitlines():
            lower,upper = map(int,each_line.split('-'))
            list_of_ranges.append((lower,upper))
        list_of_ranges.sort()
    return list_of_ranges

def find_smallest(list_of_ranges):
    floor = 0
    for each in list_of_ranges:
        if floor < each[0]:
            return floor
        floor = max(each[1] + 1, floor) 
    return None


print(find_smallest(construct_list()))

