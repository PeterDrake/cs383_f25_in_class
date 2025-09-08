def fibo_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

def fibo_iter(n):
    fibos = [0, 1]
    while len(fibos) <= n:
        fibos.append(fibos[-1] + fibos[-2])
    return fibos[n]

def fibo_small_helper(a, b, n):
    if n == 1:
        return b
    return fibo_small_helper(b, a + b, n - 1)

def fibo_small(n):
    if n == 0:
        return 0
    return fibo_small_helper(0, 1, n)

def fibo_formula(n):
    phi = (1 + 5**0.5) / 2
    return round((phi**n - (1 - phi)**n)/ 5**0.5)

if __name__ == '__main__':
    # for n in range(10):
    #     print(fibo_rec(n))
    print(fibo_formula(400))