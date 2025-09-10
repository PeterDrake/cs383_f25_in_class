# def pow(x, y):
#     v = x
#     while y > 1:
#         v = v * x
#         y = y - 1
#     return v

def pow(a, b):
    res = 1
    # for _ in range(b):
    #     res *= a
    # # return res
    if b == 0:
        return 1
    elif b % 2 == 0:
        r = pow(a, b // 2)
        return r * r
    else:
        r = pow(a, (b - 1) // 2)
        return a * r * r

