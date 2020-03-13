puzzle = '''1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0'''

operations = {1: lambda x,y : x+y, 2: lambda x,y: x*y}

def execute(p,noun,verb):
    p[1], p[2] = noun, verb
    pos = 0
    while True:
        opCode, noun, verb, result  = p[pos:pos+4]
        if opCode == 99:
            return p[0]
        p[result] = operations[opCode](p[noun],p[verb])
        pos += 4

def solve(puzzle,part=1):
    p = list(map(int,puzzle.split(',')))
    if part == 1:
        return execute(p,12,2)

    elif part == 2:
        for i in range(100):
            for j in range(100):
                if execute(p[:],i,j) == 19690720:
                    return 100*i+j
        
    
    

print(solve(puzzle,2))

