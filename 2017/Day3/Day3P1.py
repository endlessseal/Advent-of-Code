data = 368078

def generate_layer():
    x = 1
    while True:
        yield x 
        if x == 1:
            x += 7
        else:
            x += 8

def solve():
    gen = generate_layer()
    value = next(gen)
    old_value = 0
    counter = 0
    while value < data:
        old_value = value
        value += next(gen)
        counter += 1
    number_of_steps = data - old_value
    quadrant = number_of_steps // counter
    
    if (quadrant % 2) != 0:
        print((number_of_steps % counter if not number_of_steps % counter == 0 else counter) + counter)
    else:
        print((abs(counter - number_of_steps % counter) if not number_of_steps % counter == 0 else counter) + counter)
    
