var = {'a':0, 'b':0, 'c':0, 'd':0}

with open('aoc12.txt','r') as fp:
    instructions = fp.read().splitlines()
    index = 0
    while index < len(instructions):
        temp_instruction = instructions[index].split()
        command = temp_instruction[0]
        from_ = temp_instruction[1]

        if command == 'cpy':
            to_ = temp_instruction[2]
            if from_.isdigit():
                var[to_] = int(from_)
            else:
                var[to_] = var[from_] 
            
        elif command == 'inc':
            var[from_] += 1

        elif command == 'dec':
            var[from_] -= 1
            
        if command == 'jnz':
            if from_.isdigit() and int(from_) != 0:
                index += int(temp_instruction[2])
            elif var[from_] != 0:
                index += int(temp_instruction[2])
            else:
                index += 1
        else:
            index += 1

    print(var['a'])
