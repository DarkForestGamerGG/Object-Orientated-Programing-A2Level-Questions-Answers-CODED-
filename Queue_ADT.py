# Queue implementation using a linked list in Python

# Node class to store data and reference to next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class
class Queue:
    def __init__(self):
        self.front = None  # front of the queue (first element)
        self.rear = None   # rear of the queue (last element)

    # -----------------------------
    # Add element to the queue
    # -----------------------------
    def enqueue(self, data):
        new_node = Node(data)

        # If queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued {data}")
            return

        # Add new node at the end of the queue
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data}")

    # -----------------------------
    # Remove element from the queue
    # -----------------------------
    def dequeue(self):
        # If queue is empty
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
            return

        removed_value = self.front.data
        self.front = self.front.next

        # If the queue becomes empty after dequeue
        if self.front is None:
            self.rear = None

        print(f"Dequeued {removed_value}")

    # -----------------------------
    # Display the queue elements
    # -----------------------------
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        current = self.front
        print("Front -> ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")


# --------------------------------
# Example Usage
# --------------------------------
if __name__ == "__main__":
    q = Queue()

    # Add items to the queue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    print("\nCurrent Queue:")
    q.display()

    # Remove items from the queue
    print("\nPerforming dequeue operations:")
    q.dequeue()
    q.display()

    q.dequeue()
    q.display()

    q.dequeue()
    q.dequeue()
    q.dequeue()  # trying to dequeue from an empty queue
