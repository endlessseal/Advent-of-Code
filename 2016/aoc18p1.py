data = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
room = []
room.append(data)
number_of_row = 40
PATTERNS = ['^^.','.^^','^..','..^']

def get_past(i):
    if i == 0 :
        c,r = room[-1][0:2]
        l = '.'
    elif i == len(data)-1:   #i is the index so if we don't go -1 we will be out of bound
        l,c = room[-1][i-1:i+1]
        r = '.'
    else:
        l,c,r = room[-1][i-1:i+2]
    
    return l,c,r 
    
def generate_floor_tile(l,c,r):
    if l+c+r in PATTERNS:
        return '^'
    return '.'

def count_clear():
    return sum(x.count('.') for x in room)

def build_new_floor():
    return ''.join([generate_floor_tile(*get_past(i)) for i in range(len(data))])

def solve():
    while True:
        if len(room) == number_of_row:
            return count_clear()
        room.append(build_new_floor())
        
if __name__=='__main__':
    print(solve())
