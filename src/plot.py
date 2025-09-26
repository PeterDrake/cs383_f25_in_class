import matplotlib.pyplot as plt

# plt.plot([n**2 for n in range(1, 101)], label='$n^2$')
# plt.plot([n for n in range(1, 101)], label='$n$')
# plt.legend()
# plt.show()

from time import time
from fibo import *


def time_function(f, n):
    start = time()
    f(n)
    return time() - start

if __name__ == '__main__':
    for f in [#fibo_rec,
              fibo_iter, fibo_small, fibo_formula]:
        plt.plot(range(1, 51), [time_function(f, n) for n in range(1, 51)], label=str(f))
    plt.legend()
    plt.show()
