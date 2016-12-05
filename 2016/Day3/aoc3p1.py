import re

def validate_triangles(sides):
    for each in range(3):  
        temp_list = sides[:]
        last_side = temp_list.pop(each)
        if sum(temp_list) <= last_side:
            return False
    return True

count = 0
with open('aoc3.txt','r') as fp:
    for each in fp:
        list_of_num = [int(x) for x in re.findall(r'\b\d+\b', each) if x.isdigit()]
        if validate_triangles(list_of_num):
            count += 1

        
        
print(count)
