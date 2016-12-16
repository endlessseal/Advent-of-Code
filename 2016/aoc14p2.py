from hashlib import md5
import time

salt = 'ihaygndm'
generated = {}
new_keys = []
deeper = 2016

def get_hash(i):
    return generated.setdefault(i, hash_it(i))

def hash_it(word):
    x = word
    for i in range(deeper):
        x = md5(str(x).encode()).hexdigest().lower()
    return x
    
def three_in_a_row(word):
    for index in range(len(word)-2):
        if word[index:index+3].count(word[index]) == 3:
            return word[index]
    return None
    
def five_in_a_row(word):
    for index in range(len(word)-4):
        if word[index:index+5].count(word[index]) == 5:
            yield word[index]

def is_key(word,index):
    a = three_in_a_row(word)
    if a:
        for inner_index in range(1+index, 1000+index):
            for each in five_in_a_row(get_hash(inner_index)):
                if a == each:
                    return True 
    return False
    
x = time.time()
index = 0
while len(new_keys) < 64:
    lookup = get_hash(index)
    if is_key(lookup,index):
        new_keys.append(index)
    index += 1 
    
print(time.time() - x)
print(new_keys[-1])

