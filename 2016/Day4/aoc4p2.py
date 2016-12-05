import string

def cshift(text,shift):
    alphabet = string.ascii_lowercase
    s_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, s_alphabet)
    return text.translate(table)

answer = []
with open('aoc4.txt','r') as fp:
    for each in fp:
        data = each.split('-')
        sector = data.pop(-1)
        sector = sector.strip('\n')
        sector,checksum = sector[0:-7], sector[3:].strip('[').strip(']')
        shifted = cshift(' '.join(data),int(sector)%26)
        if 'pole' in shifted:
            print(sector)
            break
        
