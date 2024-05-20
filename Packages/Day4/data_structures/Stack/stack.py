class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

# Example usage:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.display()
# stack.pop()
# stack.display()
# print(stack.peek())
# print(stack.is_empty())
