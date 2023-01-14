class Node:

    def __init__(self, element=None):
        self.head = element
        self.tail = None

    def enqueue(self, element):
        if self.tail is None:
            self.tail = Node(element)
        else:
            self.tail.enqueue(element)

    def __str__(self):
        if self.head is None:
            return "end node"
        else:
            return str(self.head) + " --> " + str(self.tail)

    def __len__(self):
        if self.tail is None:
            return 1
        else:
            return 1 + len(self.tail)

class Queue:

    def __init__(self):
        self.front = None

    def enqueue(self, element):
        if self.front is None:
            self.front = Node(element)
        else:
            self.front.enqueue(element)

    def dequeue(self):
        if self.front is None:
            return None
        else:
            front = self.front.head
            self.front = self.front.tail
            return front

    def __repr__(self):
        if self.front is None:
            return "empty queue"
        else:
            return str(self.front)

    def __len__(self):
        if self.front is None:
            return 0
        else:
            return len(self.front)