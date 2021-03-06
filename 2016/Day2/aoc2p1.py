grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

normalize_list = [0,1,2]
direction = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
answer = []
s_x, s_y = 1,1

secret_code = '''LLLRLLULLDDLDUDRDDURLDDRDLRDDRUULRULLLDLUURUUUDLUUDLRUDLDUDURRLDRRRUULUURLUDRURULRLRLRRUULRUUUDRRDDRLLLDDLLUDDDLLRLLULULRRURRRLDRLDLLRURDULLDULRUURLRUDRURLRRDLLDDURLDDLUDLRLUURDRDRDDUURDDLDDDRUDULDLRDRDDURDLUDDDRUDLUDLULULRUURLRUUUDDRLDULLLUDLULDUUDLDLRRLLLRLDUDRUULDLDRDLRRDLDLULUUDRRUDDDRDLRLDLRDUDRULDRDURRUULLUDURURUUDRDRLRRDRRDRDDDDLLRURULDURDLUDLUULDDLLLDULUUUULDUDRDURLURDLDDLDDUULRLUUDLDRUDRURURRDDLURURDRLRLUUUURLLRR
UUUUURRRURLLRRDRLLDUUUUDDDRLRRDRUULDUURURDRLLRRRDRLLUDURUDLDURURRLUDLLLDRDUDRDRLDRUDUDDUULLUULLDUDUDDRDUUUDLULUDUULLUUULURRUDUULDUDDRDURRLDDURLRDLULDDRUDUDRDULLRLRLLUUDDURLUUDLRUUDDLLRUURDUDLLDRURLDURDLRDUUDLRLLRLRURRUDRRLRDRURRRUULLUDLDURDLDDDUUDRUUUDULLLRDRRDRLURDDRUUUDRRUUDLUDDDRRRRRLRLDLLDDLRDURRURLLLULURULLULRLLDDLDRLDULLDLDDDRLUDDDUDUDRRLRDLLDULULRLRURDLUDDLRUDRLUURRURDURDRRDRULUDURRLULUURDRLDLRUDLUDRURLUDUUULRRLRRRULRRRLRLRLULULDRUUDLRLLRLLLURUUDLUDLRURUDRRLDLLULUDRUDRLLLRLLDLLDUDRRURRLDLUUUURDDDUURLLRRDRUUURRRDRUDLLULDLLDLUDRRDLLDDLDURLLDLLDLLLDR
LRDULUUUDLRUUUDURUUULLURDRURDRRDDDLRLRUULDLRRUDDLLUURLDRLLRUULLUDLUDUDRDRDLUUDULLLLRDDUDRRRURLRDDLRLDRLULLLRUUULURDDLLLLRURUUDDDLDUDDDDLLLURLUUUURLRUDRRLLLUUULRDUURDLRDDDUDLLRDULURURUULUDLLRRURDLUULUUDULLUDUUDURLRULRLLDLUULLRRUDDULRULDURRLRRLULLLRRDLLDDLDUDDDUDLRUURUDUUUDDLRRDLRUDRLLRDRDLURRLUDUULDRRUDRRUDLLLLRURRRRRUULULLLRDRDUDRDDURDLDDUURRURLDRRUDLRLLRRURULUUDDDLLLRDRLULLDLDDULDLUUDRURULLDLLLLDRLRRLURLRULRDLLULUDRDR
RURRRUDLURRURLURDDRULLDRDRDRRULRRDLDDLDUUURUULLRRDRLDRRDRULLURRRULLLDULDDDDLULRUULRURUDURDUDRLRULLLRDURDDUDDRDLURRURUURDLDDDDDURURRURLLLDDLDRRDUDDLLLDRRLDDUUULDLLDRUURUDDRRLDUULRRDDUDRUULRLDLRLRUURLLDRDLDRLURULDLULDRULURLLRRLLDDDURLRUURUULULRLLLULUDULUUULDRURUDDDUUDDRDUDUDRDLLLRDULRLDLRRDRRLRDLDDULULRLRUUDDUDRRLUDRDUUUDRLLLRRLRUDRRLRUUDDLDURLDRRRUDRRDUDDLRDDLULLDLURLUUDLUDLUDLDRRLRRRULDRLRDUURLUULRDURUDUUDDURDDLRRRLUUUDURULRURLDRURULDDUDDLUDLDLURDDRRDDUDUUURLDLRDDLDULDULDDDLDRDDLUURDULLUDRRRULRLDDLRDRLRURLULLLDULLUUDURLDDULRRDDUULDRLDLULRRDULUDUUURUURDDDRULRLRDLRRURR
UDDDRLDRDULDRLRDUDDLDLLDDLUUURDDDLUDRDUDLDURLUURUDUULUUULDUURLULLRLUDLLURUUUULRLRLLLRRLULLDRUULURRLLUDUDURULLLRRRRLRUULLRDRDRRDDLUDRRUULUDRUULRDLRDRRLRRDRRRLULRULUURRRULLRRRURUDUURRLLDDDUDDULUULRURUDUDUDRLDLUULUDDLLLLDRLLRLDULLLRLLDLUUDURDLLRURUUDDDDLLUDDRLUUDUDRDRLLURURLURRDLDDDULUURURURRLUUDUDLDLDDULLURUDLRLDLRLDLDUDULURDUDRLURRRULLDDDRDRURDDLDLULUDRUULDLULRDUUURLULDRRULLUDLDRLRDDUDURRRURRLRDUULURUUDLULDLRUUULUDRDRRUDUDULLDDRLRDLURDLRLUURDRUDRDRUDLULRUDDRDLLLRLURRURRLDDDUDDLRDRRRULLUUDULURDLDRDDDLDURRLRRDLLDDLULULRRDUDUUDUULRDRRDURDDDDUUDDLUDDUULDRDDULLUUUURRRUUURRULDRRDURRLULLDU'''.split('\n')

for each in secret_code:
    for every in each:
        s_x, s_y = min(normalize_list, key=lambda x:abs(x-(s_x+direction[every][0]))),min(normalize_list, key=lambda x:abs(x-(s_y+direction[every][1])))
    answer.append(grid[s_x][s_y])
print(answer)
        
