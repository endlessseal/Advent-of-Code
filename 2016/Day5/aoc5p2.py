from hashlib import md5
from itertools import takewhile,count

def generate_hash(i):
    d_id = 'ugkcyxxp'
    while True:
        yield md5((d_id+str(i)).encode()).hexdigest()

answer = [None]*8        
for i in takewhile(lambda c: any(a is None for a in answer), count()):
    hashed = str(next(generate_hash(i)))
    if hashed[0:5] == '00000':
        if hashed[5].isdigit():
            temp_location = int(hashed[5])
            if temp_location < len(answer) and not answer[temp_location]:
                answer[temp_location] = hashed[6]


password=''.join(answer)
print(password)



                

