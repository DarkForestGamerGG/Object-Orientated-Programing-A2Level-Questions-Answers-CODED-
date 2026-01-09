# Singly Linked List implementation in Python

# Node class - represents each element in the list
class Node:
    def __init__(self, data):
        self.data = data     # store data
        self.next = None     # pointer to the next node


# Linked List class - manages the whole list
class LinkedList:
    def __init__(self):
        self.head = None  # initially, the list is empty

    # -----------------------------
    # Insert a new element at the end
    # -----------------------------
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # first node in the list
        else:
            current = self.head
            while current.next:  # move to the end
                current = current.next
            current.next = new_node

    # -----------------------------
    # Search for an element
    # -----------------------------
    def search(self, key):
        current = self.head
        position = 0  # optional: track position
        while current:
            if current.data == key:
                return f"Item {key} found at position {position}"
            current = current.next
            position += 1
        return f"Item {key} not found in the list."

    # -----------------------------
    # Delete an element by value
    # -----------------------------
    def delete(self, key):
        current = self.head
        previous = None

        # Case 1: List is empty
        if current is None:
            print("The list is empty.")
            return

        # Case 2: The node to delete is the head
        if current.data == key:
            self.head = current.next
            print(f"Deleted {key} from the list.")
            return

        # Case 3: Search for the node to delete
        while current and current.data != key:
            previous = current
            current = current.next

        # Key not found
        if current is None:
            print(f"Item {key} not found in the list.")
            return

        # Unlink the node
        previous.next = current.next
        print(f"Deleted {key} from the list.")

    # -----------------------------
    # Display the list contents
    # -----------------------------
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# --------------------------------
# Example Usage
# --------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Add data to the linked list
    items = [10, 20, 30, 40, 50]
    for item in items:
        ll.insert(item)

    print("Initial linked list:")
    ll.display()

    # Search for elements
    print(ll.search(30))
    print(ll.search(100))

    # Delete elements
    ll.delete(20)
    ll.display()

    ll.delete(50)
    ll.display()

    ll.delete(100)  # trying to delete a non-existing value
