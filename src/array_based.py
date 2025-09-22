class ArrayList:

    def __init__(self):
        self._data = [None]
        self._size = 0

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, item):
        self._data[index] = item

    def __len__(self):
        return self._size

    def __repr__(self):
        result = '<'
        if self._size > 0:
            result += self._data[0]
        for i in range(1, self._size):
            result += ', ' + self._data[i]
        return result + '>'

    def add_at(self, index, item):
        if self._size == len(self._data):
            self._expand()
        for j in range(self._size, index, -1):
            self._data[j] = self._data[j - 1]
        self._data[index] = item
        self._size += 1

    def remove_at(self, index):
        for j in range(index, self._size - 1):
            self._data[j] = self._data[j + 1]
        self._size -= 1

    def _expand(self):
        new_data = [None] * self._size * 2
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data