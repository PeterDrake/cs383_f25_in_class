from fibo import *

def test_works_recursively():
    assert fibo_rec(7) == 13

def test_works_iteratively():
    assert fibo_iter(7) == 13
