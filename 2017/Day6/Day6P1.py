data = '''0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'''

def solve(x):
    memory = [int(y) for y in x.split('\t')]
    memory_count = len(memory)
    count = 0
    seen_pattern = []
    
    while True:
        mem_block_amount = max(memory)
        mem_block_index = memory.index(mem_block_amount)
        memory[mem_block_index] = 0
        for _ in range(mem_block_amount):
            mem_block_index += 1
            memory[mem_block_index % memory_count] += 1
        count += 1
        if memory in seen_pattern:
            return count 
        else:
            seen_pattern.append(memory[:])

print(solve(data))
