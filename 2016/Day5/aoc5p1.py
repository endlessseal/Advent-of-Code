from hashlib import md5
from itertools import takewhile,count
def generate_hash(i):
    d_id = 'ugkcyxxp'
    while True:
        yield md5((d_id+str(i)).encode()).hexdigest()

answer = []        
for i in takewhile(lambda c: len(answer) <8, count()):
    hashed = str(next(generate_hash(i)))
    if hashed[0:5] == '00000':
        answer.append(hashed)
password=''
for each in answer:
    password += each[5]
print(password)

