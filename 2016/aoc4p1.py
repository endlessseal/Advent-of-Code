from collections import Counter

total = 0
with open('aoc4.txt','r') as fp:
    for each in fp:
        data = each.split('-')
        sector = data.pop(-1)
        sector = sector.strip('\n')
        sector,checksum = sector[0:-7], sector[3:].strip('[').strip(']')
        counted = sorted(Counter(''.join(data)).most_common(), key=lambda x: (-x[1], x[0]))
        values = ''
        for each in counted[0:5]:
            values += each[0]
        if values == checksum:
            total += int(sector)
print(total)
