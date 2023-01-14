class Node:

    def __int__(self, element=None):
        self.head = element
        self.tail = None

    def enqueue(self, node):
        if self.tail is None:
            self.tail = node
        else:
            self.tail.enqueue(node)


class Queue:

    def __int__(self):
        self.front = None

    def enqueue(self, node):
        if self.front is None:
            self.front = node
        else:
            self.front.enqueue(node)

    def dequeue(self):
        front = self.front.head
        self.front = self.front.tail
        return front

