class SmallSet:
    def __init__(self):
        self.data = [False] * 100

    def add(self, key):
        self.data[key] = True

    def contains(self, key):
        return self.data[key]

    def remove(self, key):
        self.data[key] = False
