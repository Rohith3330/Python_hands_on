class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, val):
        current = self.head
        if not current:
            return
        if current.val == val:
            self.head = current.next
            return
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next

    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example usage:
# linked_list = LinkedList()
# linked_list.insert(1)
# linked_list.insert(2)
# linked_list.display()
# linked_list.delete(1)
# linked_list.display()
# print(linked_list.search(2))
