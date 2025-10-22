class Node():
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = None

c = Node('c', None, None)
d = Node('d', None, None)
b = Node('b', c, d)
a = Node('a', None, None)
e = Node('e', a, b)

t = BinaryTree()
t.root = e
