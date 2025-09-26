def linear_search(key, ls):
    for i, x in enumerate(ls):
        if x == key:
            return i
    return -1


def binary_search(key, ls):
    lo = 0
    hi = len(ls) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < ls[mid]:
            hi = mid - 1
        elif key == ls[mid]:
            return mid
        else:
            lo = mid + 1
    return -1


def interpolation_search(key, ls):
    lo = 0
    hi = len(ls) - 1
    while lo <= hi:
        if lo == hi:
            if key == ls[lo]:
                return lo
            else:
                return -1
        fraction = (key - ls[lo]) / (ls[hi] - ls[lo])
        mid = int(lo + (hi - lo) * fraction)
        mid = max(lo, min(hi, mid))  # Because the formula could produce a value out of this range
        if key < ls[mid]:
            hi = mid - 1
        elif key == ls[mid]:
            return mid
        else:
            lo = mid + 1
    return -1

import matplotlib.pyplot as plt
import random
from time import time

def time_search(f, n):
    ls = [random.random() for _ in range(n)]
    ls = sorted(ls)
    key = random.random()
    start = time()
    f(key, ls)
    return time() - start

if __name__ == '__main__':
    for f in [#linear_search,
              binary_search, interpolation_search]:
        plt.plot([2**n for n in range(25)], [time_search(f, 2**n) for n in range(25)], label=str(f))
    plt.legend()
    plt.show()
