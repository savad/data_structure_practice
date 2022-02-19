from collections import defaultdict
from itertools import islice


def prime_generator():
    memory = defaultdict(list)
    p = 2

    while True:
        if p not in memory:
            yield p
            memory[2 * p].append(p)
        else:
            for f in memory[p]: # [3]
                memory[p + f].append(f)
                # 
    
        p += 1

prime_gen = prime_generator()
print([next(prime_gen) for i in range(10)])
