import numpy as np

board = np.zeros((6,50),dtype='int')

with open('aoc8.txt','r') as fp:
    for each_line in i.splitlines():
        each_line = each_line.split(' ')
        if each_line[0] == 'rect':
            setting = each_line[1].split('x')
            board[np.ix_(np.arange(int(setting[1])), np.arange(int(setting[0])))] = 1
        else:
            selector = each_line[1]
            index = int(each_line[2][2:])
            amount_to_roll = int(each_line[4])
            if selector == 'row':
                board[index] = np.roll(board[index],amount_to_roll)
            else:
                board[:,index] = np.roll(board[:,index],amount_to_roll)

for row in board:
    for each in row:
        if each == 0:
            print(' ', end='')
        else:
            print('*', end='')
