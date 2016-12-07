import re

def get_chunks(word):
    count = 0
    while len(word[count:count+4]) == 4:
        yield word[count:count+4]
        count += 1

def checkABBA(word):
    a,b,c,d = word
    if a == d and b == c and a != b:
        return True
    return False

def validate(word):
    for each in get_chunks(word):
        if checkABBA(each):
            return True
    return False
        
count = 0
with open('aoc7.txt','r') as fp:
    for each_line in fp.read().splitlines():
        if not any(map(validate,re.findall(r'\[([a-z]*)\]',each_line))):
            if any(map(validate,[s.split(']')[-1] for s in each_line.split('[')])):
                count += 1
print(count)

                
            
