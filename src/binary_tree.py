from collections import deque

class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self):
        self.root = None

    def level_order(self):
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            node = q.popleft()
            print(node.key)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def preorder(self):
        s = []  # A stack rather than a queue
        s.append(self.root)
        while len(s) > 0:
            node = s.pop()
            print(node.key)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)

    def preorder(self):
        def f(node):
            print(node.key)
            if node.left is not None:
                f(node.left)
            if node.right is not None:
                f(node.right)
        f(self.root)

    def inorder(self):
        def f(node):
            if node.left is not None:
                f(node.left)
            print(node.key)
            if node.right is not None:
                f(node.right)
        f(self.root)

    def postorder(self):
        def f(node):
            if node.left is not None:
                f(node.left)
            if node.right is not None:
                f(node.right)
            print(node.key)
        f(self.root)

c = Node('c')
d = Node('d')
b = Node('b', c, d)
f = Node('f')
g = Node('g')
a = Node('a', f, g)
e = Node('e', a, b)

t = BinaryTree()
t.root = e
# t.level_order()
# t.preorder()
# t.inorder()
t.postorder()
