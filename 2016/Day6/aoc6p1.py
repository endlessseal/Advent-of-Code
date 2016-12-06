import string

x = [{a:0 for a in string.ascii_lowercase} for x in range(8)]
answer = ''
with open('aoc6.txt','r') as fp:
    for each_line in fp:
        for index,letters in enumerate(each_line.strip('\n')):
            x[index][letters] += 1
for every_letter in x:
    answer += max(every_letter, key= lambda k: every_letter[k])
    
print(answer)
