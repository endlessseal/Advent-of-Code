number = 1350

class Node:
    def __init__(self,location,typing='.'):
        self.location = location
        self.from_ = None
        self.typing = typing
        self.H = 0
        self.G = 0
    def move(self,other):
        if self.typing == '.':
            return 0
        else:
            return 1
'''
def generate_maze(number):
    maze = [[Node('#',(y,x)) if sum(map(int,bin(x*x + 3*x + 2*x*y + y + y*y + number)[2:])) % 2 == 1 else Node('.',(y,x)) for x in range(number)] for y in range(number)]

    #just for the sake of readability:
    row = []
    maze = []
    equation = lambda x,y,number: x*x + 3*x + 2*x*y + y + y*y + number
    for y in range(number):
        for x in range(number):
            binary = bin(equation(x,y,number))[2:]
            number_of_ones = sum(map(int,binary))
            if number_of_ones %2 == 1:
                row.append(Node('#',(x,y)))
            else:
                row.append(Node('.',(x,y)))
        maze.append(row)
        row = []
    
    return maze
'''

def is_not_wall(x,y):
    return bin(x*x + 3*x + 2*x*y + y + y*y + number).count('1') % 2 == 0

def neighbours(coords):
    y,x = coords.location
    for temp_y, temp_x in [(1,0),(0,1),(-1,0),(0,-1)]:
        next_x, next_y = x + temp_x, y + temp_y
        if is_not_wall(next_x, next_y) and next_x >=0 and next_y >=0:
            yield (next_y, next_x)
        
def find_path(node):
    path = []
    while node.from_:
        path.append(node)
        node = node.from_
    path.append(node)
    return path

def cal_h(node, goal):
    n_y, n_x = node.location
    g_y, g_x = goal
    return abs(n_y - g_y) + abs(n_x - g_x)

def find_in_closed(location,closed):
    for each in closed:
        if location == each.location:
            return True
    return False

def find_in_available(location,available):
    for each in available:
        if location == each.location:
            return True
    return False

def a_star(goal):
    closed = set()
    available = set()
    available.add(Node((1,1)))#the starting point

    while available:
        current = min(available, key=lambda x: x.G + x.H)
        if current.location == goal:
            return find_path(current)
        available.remove(current)
        closed.add(current)
        for each_node in neighbours(current):
            if find_in_closed(each_node,closed):
                continue
            each_node = Node(each_node)
            if find_in_available(each_node,available):
                g = current.G + current.move(each_node)
                if each_node.G > g:
                    each_node.G = g
                    each_node.from_ = current
            else:
                each_node.G = current.G + current.move(each_node)
                each_node.H = cal_h(each_node, goal)
                each_node.from_ = current
                available.add(each_node)



found = a_star((39,31))
print(len(found)-1)

            
    
        
