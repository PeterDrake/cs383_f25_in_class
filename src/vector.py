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

v = Vector(3, 4)
w = Vector(10, 20)
z = v + w

print(z)
