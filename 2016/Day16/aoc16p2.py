length = 35651584
data = '10010000000110000'
import time

def timing(func):
    def wrapper(*arg, **kw):
        x = time.time()
        res = func(*arg,**kw)
        print(time.time()-x,func.__name__)
        return res
    return wrapper

@timing
def transform(x):
    return ''.join(['0' if i == '1' else '1' for i in reversed(x)])

@timing
def dragoon(data):
    while True:
        if len(data) >= length:
            return data[0:length]
        data = data + '0' + transform(data)

@timing
def check_sum(data):  
    while True:
        if len(data) % 2 == 1:
            return data
        data = ''.join(['1' if i == '11' or i == '00' else '0' for i in (data[k:k+2] for k in range(0,len(data),2))])
        
        
def main():
    print(check_sum(dragoon(data)))

if __name__=='__main__':

    x = time.time()
    main()
    print(time.time() - x)
    
