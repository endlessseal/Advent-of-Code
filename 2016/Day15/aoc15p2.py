x = '''Disc #1 has 17 positions; at time=0, it is at position 15.
Disc #2 has 3 positions; at time=0, it is at position 2.
Disc #3 has 19 positions; at time=0, it is at position 4.
Disc #4 has 13 positions; at time=0, it is at position 2.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 5 positions; at time=0, it is at position 0.'''
import re
data = [map(int,i) for i in (re.findall(r'\d+', k) for k in x.splitlines())]
data.append([7,11,0,0]) 
def counting(i = 0):
    while True:
        yield i
        i+=1
        
def is_hole(disk, num_pos, time, pos):
    return (time+pos+disk+1) % num_pos == 0

def find_time_for_hole(data):
    for time in counting():
        if all(is_hole(disk, num_pos, time, pos) for disk, (_, num_pos, _, pos) in enumerate(data)):
            return time

print(find_time_for_hole(data))
