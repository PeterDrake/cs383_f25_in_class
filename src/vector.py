class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        # return '<' + str(self.x) + ', ' + str(self.y) + '>'
        return f'<{self.x}, {self.y}>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

a = Vector(3, 4)
b = Vector(10, 20)
c = Vector(10, 20)
print(hash(a))
print(hash(b))
print(hash(c))

