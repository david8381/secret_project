from numba import njit, prange
import time


@njit(parallel=True)
def with_numba_parallel(n):
    x = 0
    for i in prange(0, 10**n):
        x = x + 1
    return x


@njit()
def with_numba(n):
    x = 0
    for i in prange(0, 10**n):
        x = x + 1
    return x


def normal(n):
    x = 0
    for i in prange(0, 10**n):
        x = x + 1
    return x

# compile code ahead of time by running functions so that the timing is accurate
with_numba(0)
with_numba_parallel(0)


n = int(input('Iterations (10**n): '))

start = time.time()
#print(normal(n)) # this can be painfully slow, commen to test other functions with higher numbers
end = time.time()
normal_time = end-start

start = time.time()
print(with_numba(n))
end = time.time()
numba_time = end-start

start = time.time()
print(with_numba_parallel(n))
end = time.time()
parallel_time = end-start

#print(f"Normal: {normal_time}")
print(f"Numba: {numba_time}")
print(f"Parallel Numba: {parallel_time}")
