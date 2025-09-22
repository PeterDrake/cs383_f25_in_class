class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self._front = None

    def __getitem__(self, index):
        node = self._front
        for i in range(index):
            node = node.next
        return node.item

    def __setitem__(self, index, item):
        node = self._front
        for i in range(index):
            node = node.next
        node.item = item

    def __len__(self):
        node = self._front
        result = 0
        while node:
            result += 1
            node = node.next
        return result

    def __repr__(self):
        result = '<'
        if self._front:
            result += self._front.item
            node = self._front.next
            while node:
                result += ', ' + node.item
                node = node.next
        return result + '>'

    def add_at(self, index, item):
        if index == 0:
            self._front = Node(item, self._front)
        else:
            node = self._front
            for i in range(index - 1):
                node = node.next
            node.next = Node(item, node.next)

    def remove_at(self, index):
        if index == 0:
            self._front = self._front.next
        else:
            node = self._front
            for i in range(index - 1):
                node = node.next
            node.next = node.next.next