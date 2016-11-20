from time import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def gcd(pair):
    # compute the greatest common divisor
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers = [(1963309, 2265973),
           (2030677, 3814172),
           (1551645, 2229620),
           (2039045, 2020802)]

# Serial Run
start = time()
results = list(map(gcd, numbers))
end = time()
print('Serial run took %.3f seconds' % (end - start))

# Multithreading yields no speed improvement because GIL prevents Python from
# using multiple CPU cores in parallel
# Overhead and communicating with the pool of threads actually make it slower
start = time()
pool = ThreadPoolExecutor(max_workers=8)
results = list(pool.map(gcd, numbers))
end = time()
print('Multithreaded took %.3f seconds' % (end - start))

# Multiprocessing
start = time()
pool = ProcessPoolExecutor(max_workers=8)
results = list(pool.map(gcd, numbers))
end = time()
print('Multiprocessed took %.3f seconds' % (end - start))
