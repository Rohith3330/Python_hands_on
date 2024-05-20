class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.val < current.val:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, current, val):
        if not current:
            return current
        if val < current.val:
            current.left = self._delete_recursive(current.left, val)
        elif val > current.val:
            current.right = self._delete_recursive(current.right, val)
        else:
            if not current.left:
                return current.right
            if not current.right:
                return current.left
            temp_val = self._find_min(current.right).val
            current.val = temp_val
            current.right = self._delete_recursive(current.right, temp_val)
        return current

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, current, val):
        if not current or current.val == val:
            return current
        if val < current.val:
            return self._search_recursive(current.left, val)
        return self._search_recursive(current.right, val)

    def display(self):
        self._display_recursive(self.root)

    def _display_recursive(self, node):
        if node:
            self._display_recursive(node.left)
            print(node.val, end=" ")
            self._display_recursive(node.right)

# Example usage:
# binary_tree = BinaryTree()
# binary_tree.insert(5)
# binary_tree.insert(3)
# binary_tree.insert(7)
# binary_tree.display()
# binary_tree.delete(3)
# binary_tree.display()
# print(binary_tree.search(5))
