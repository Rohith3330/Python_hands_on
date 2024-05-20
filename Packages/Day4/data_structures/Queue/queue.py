class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

# Example usage:
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.display()
# queue.dequeue()
# queue.display()
# print(queue.front())
# print(queue.is_empty())
