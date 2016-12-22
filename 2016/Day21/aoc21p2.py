from collections import deque

def swap(word, pos1, pos2):
    word[pos2], word[pos1] = word[pos1], word[pos2]
    return word

def replace_letters(word,letter1,letter2):
    lookup = {letter1:letter2, letter2:letter1}
    return[i if i not in lookup else lookup[i] for i in word]

def rotate(word,i):
    to_rotate = deque(word)
    to_rotate.rotate(i*(-1))
    return(list(to_rotate))

def move(word,x,y):
    letter = word[y]
    del word[y]
    word.insert(x,letter)
    return word

def reverse(word,x,y):
    reverse = reversed(word[x:y+1])
    return word[0:x] + list(reverse) + word[y+1:]

def solve():
    to_scramble = list('fbgdceah')
    rotate_lookup = {'right':1, 'left':-1}
    rotate_pos = {'1':1,'3':2,'5':3,'7':4,'2':6,'4':7,'6':0,'0':1}
    
    with open('aoc21.txt','r') as fp:
        for each_line in reversed(fp.read().splitlines()):
            instruction = each_line.split()
            func = instruction[0]

            if func == 'swap':
                mode = instruction[1]
                swap1 = instruction[2]
                swap2 = instruction[5]

                if mode == 'position':
                    to_scramble = swap(to_scramble, int(swap1), int(swap2))
                else:
                    to_scramble = replace_letters(to_scramble, swap1, swap2)
        
            elif func == 'reverse':
                rev1 = int(instruction[2])
                rev2 = int(instruction[4])

                to_scramble = reverse(to_scramble, rev1, rev2)

            elif func == 'move':
                pos1 = int(instruction[2])
                pos2 = int(instruction[5])

                to_scramble = move(to_scramble, pos1, pos2)

            elif func == 'rotate':
                mode = instruction[1]

                if mode == 'based':
                    letter = instruction[6]
                    index = to_scramble.index(letter)
                    value = rotate_pos[str(index)]

                    to_scramble = rotate(to_scramble,value)

                else:
                    value = int(instruction[2])*rotate_lookup[mode]

                    to_scramble = rotate(to_scramble,value)

        return ''.join(to_scramble)

print(solve())
