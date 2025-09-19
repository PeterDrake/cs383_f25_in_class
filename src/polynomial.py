def eval_pol(x, coefficients):
    result = 0
    for i, c in enumerate(coefficients):
        term = c
        for j in range(i):
            term *= x
        result += term
    return result

print(eval_pol(2, [4, 3, 2]))

def horner(x, coefficients):
    if len(coefficients) == 1:
        return coefficients[0]
    else:
        return x * horner(x, coefficients[1:]) + coefficients[0]

print(horner(2, [4, 3, 2]))
