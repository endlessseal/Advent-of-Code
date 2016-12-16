number = 1350
def is_not_wall(x,y):
    return bin(x*x + 3*x + 2*x*y + y + y*y + number).count('1') % 2 == 0


def neighbours(coords):
    y,x = coords
    for temp_y, temp_x in [(1,0),(0,1),(-1,0),(0,-1)]:
        next_x, next_y = x + temp_x, y + temp_y
        if is_not_wall(next_x, next_y) and next_x >=0 and next_y >=0:
            yield (next_y, next_x)
            

def find_paths():
    closed = set()
    available = set()
    available.add((1,1))#the starting point
    depth = 0
    while available and depth < 50:
        temp_ava = set()
        for each_node in available:
            for i in neighbours(each_node):
                if i not in closed:
                    temp_ava.add(i)
        closed = closed.union(available)
        available = temp_ava
        depth += 1
    return closed.union(available)

print(len(find_paths()))
