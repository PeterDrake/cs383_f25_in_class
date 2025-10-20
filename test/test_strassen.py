from strassen import mult, add, sub

def test_multiplies_1x1():
    a = [[3]]
    b = [[4]]
    assert mult(a, b) == [[12]]

def test_multiplies_2x2():
    a = [[3, 4], [5, 6]]
    b = [[8, 6], [1, 0]]
    correct = [[28, 18], [46, 30]]
    assert mult(a, b) == correct

def test_adds_2x2():
    a = [[3, 4], [5, 6]]
    b = [[8, 6], [1, 0]]
    correct = [[11, 10], [6, 6]]
    assert add(a, b) == correct

def test_subtract_2x2():
    a = [[3, 4], [5, 6]]
    b = [[8, 6], [1, 0]]
    correct = [[-5, -2], [4, 6]]
    assert sub(a, b) == correct