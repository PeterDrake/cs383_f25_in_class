# def dot_product(a,b):
#     tot = 0
#     for i in range(len(a)):
#         tot += a[i] * b[i]
#     return tot
#
# def dot_product(a,b):
#     return sum(x * y for x, y in zip(a, b))
#
# print(dot_product([3, 5, 2], [4, 1, 6]))

def dot_product(a, b):
    la = len(a)
    r = 0
    for i in range(la):
        r += a[i] * b[i]
    return r


def matrix_product(m, n):
    result = [[0] * len(n[0]) for l in range(len(m))]  # makes 0 matrix of n column rows and m row columns
    for i in range(len(m)):  # how many rows in m
        for j in range(len(n[0])):  # columns of n
            total = 0
            for k in range(len(n)):  # rows in n = columns in m
                total += m[i][k] * n[k][j]
            result[i][j] = total  # updates 0's in matrix
    return result


def main():
    a = [3, 1, 5]
    b = [3, 2, 1]
    c = [[3, 4], [5, 6]]
    d = [[8, 6], [1, 0]]
    print(dot_product(a, b))
    print(matrix_product(c, d))


# test to make sure it works
if __name__ == "__main__":
    main()