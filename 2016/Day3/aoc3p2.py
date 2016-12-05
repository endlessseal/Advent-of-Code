import re

def validate_triangles(sides):
    for each in range(3):  
        temp_list = sides[:]
        last_side = temp_list.pop(each)
        if sum(temp_list) <= last_side:
            return False
    return True

count = 0
list_of_triangles = []
with open('aoc3.txt','r') as fp:
    for index, each in enumerate(fp,1):
        list_of_num = [int(x) for x in re.findall(r'\b\d+\b', each) if x.isdigit()]
        list_of_triangles.append(list_of_num)
        
        if index % 3 == 0 and index != 0:
            for i,j,k in zip(*list_of_triangles):
                if validate_triangles([i,j,k]):
                    count += 1
            list_of_triangles = []
print(count)
