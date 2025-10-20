def add(a, b):
    return [[x + y for x, y in zip(a_, b_)] for a_, b_ in zip(a, b)]

def sub(a, b):
    return [[x - y for x, y in zip(a_, b_)] for a_, b_ in zip(a, b)]

def mult(a, b):
    """
    Returns the product of matrices a and b. Both are assumed to
    be n x n, where n is a positive power of 2.
    """
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
    # Extract submatrices
    a_ = {}  # Quarters of a
    b_ = {}  # Quarters of b
    for i in (0, 1):
        for j in (0, 1):
            a_[(i, j)] = [row[j * (n//2) : (j+1) * n // 2]
                               for row in a[i * (n//2) : (i+1) * n // 2]]
            b_[(i, j)] = [row[j * (n//2) : (j+1) * n // 2]
                               for row in b[i * (n//2) : (i+1) * n // 2]]
    # Compute terms
    m1 = mult(add(a_[(0, 0)], a_[(1, 1)]),
              add(b_[(0, 0)], b_[(1, 1)]))
    m2 = mult(add(a_[(1, 0)], a_[(1, 1)]),
              b[(0, 0)])
    m3 = mult(a[(0, 0)],
              sub(b_[(0, 1)], b_[(1, 1)]))
    m4 = mult(a[(1, 1)],
              sub(b_[(1, 0)], b_[(0, 0)]))
    m5 = mult(add(a_[(0, 0)], a_[(0, 1)]),
              b_[(1, 1)])
    m6 = mult(sub(a_[(1, 0)], a_[(0, 0)]),
              add(b_[(0, 0)], b_[(0, 1)]))
    m7 = mult(sub(a_[(0, 1)], a_[(0, 0)]),
              add(b_[(1, 0)], b_[(1, 1)]))
    # Combine results

    # Return result
