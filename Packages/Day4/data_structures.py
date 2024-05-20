from data_structures.Linked_list.linked_list import LinkedList
from data_structures.Stack.stack import Stack
from data_structures.Queue.queue import Queue
from data_structures.Binary_tree.binary_tree import BinaryTree

def main():
    # Linked List
    print("Linked List:")
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.display()
    linked_list.delete(2)
    linked_list.display()
    print("Search 3:", linked_list.search(3))

    # Stack
    print("\nStack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.display()
    print("Peek:", stack.peek())
    print("Is Empty:", stack.is_empty())

    # Queue
    print("\nQueue:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    queue.dequeue()
    queue.display()
    print("Front:", queue.front())
    print("Is Empty:", queue.is_empty())

    # Binary Tree
    print("\nBinary Tree:")
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.display()
    print()
    binary_tree.delete(3)
    binary_tree.display()
    print()
    print("Search 7:", binary_tree.search(7) is not None)

if __name__ == "__main__":
    main()
