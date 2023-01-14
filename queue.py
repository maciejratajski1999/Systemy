class Node:

    def __init__(self, element=None):
        self.head = element
        self.tail = None

    def enqueue(self, node):
        if self.tail is None:
            self.tail = Node(element)
        else:
            self.tail.enqueue(node)

    def __str__(self):
        if self.head is None:
            return "end node"
        else:
            return str(self.head) + " --> " + str(self.tail)

class Queue:

    def __init__(self):
        self.front = None

    def enqueue(self, element):
        if self.front is None:
            self.front = Node(element)
        else:
            self.front.enqueue(element)

    def dequeue(self):
        front = self.front.head
        self.front = self.front.tail
        return front

    def __repr__(self):
        if self.front is None:
            return "empty queue"
        else:
            return str(self.front)