import re

def get_chunks(word):
    count = 0
    while len(word[count:count+3]) == 3:
        yield word[count:count+3]
        count += 1

def checkABA(word):
    a,b,c = word
    if a == c and a != b:
        return True
    return False

def validate(word):
    palli = []
    for each in get_chunks(word):
        if checkABA(each):
            if each not in palli:
                palli.append(each)
    return palli

def relationship(l1,l2):
    for each in l1:
        for every in l2:
            if each[0:1] == every[1:2]:
                return True
    return False

count = 0
with open('aoc7.txt','r') as fp:
    for each_line in fp.read().splitlines():
        sb = map(validate,re.findall(r'\[([a-z]*)\]',each_line))
        nsb = map(validate,[s.split(']')[-1] for s in each_line.split('[')])
        if relationship([y for x in sb for y in x if x], [y for x in nsb for y in x if x]):
            count += 1
print(count)

                
            
