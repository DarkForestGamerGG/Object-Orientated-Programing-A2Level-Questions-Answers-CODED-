# Binary Search Tree implementation in Python

# Node class to represent each element in the tree
class Node:
    def __init__(self, value):
        self.value = value      # data stored in the node
        self.left = None        # left child
        self.right = None       # right child


# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None  # initially tree is empty

    # Method to insert a new node
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
        else:
            # value already exists in the tree
            print(f"Value {value} already exists in the tree!")

    # Method to search for a value in the tree
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None:
            return False  # value not found
        elif current_node.value == value:
            return True  # value found
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)

    # Helper method for displaying the tree in-order (sorted order)
    def inorder_traversal(self):
        elements = []
        self._inorder(self.root, elements)
        return elements

    def _inorder(self, node, elements):
        if node:
            self._inorder(node.left, elements)
            elements.append(node.value)
            self._inorder(node.right, elements)


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Add data to the binary tree
    data_items = [50, 30, 70, 20, 40, 60, 80]
    for item in data_items:
        bst.insert(item)

    # Display tree elements in sorted order
    print("In-order traversal of the tree:", bst.inorder_traversal())

    # Search for values in the tree
    search_items = [40, 25, 70]
    for item in search_items:
        found = bst.search(item)
        print(f"Search for {item}: {'Found' if found else 'Not Found'}")
