# Task 1 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Optional but recommended
        self.size = 0
        print("Created new LinkedList")
        self.display_status()

    def display_status(self):
        print(f"Current size: {self.size}")
        print(f"Head: {self.head.data if self.head else 'None'}")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()

# Task 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Optional but recommended
        self.size = 0
        print("Created new LinkedList")
        self.display_status()

    def display_status(self):
        print(f"Current size: {self.size}")
        print(f"Head: {self.head.data if self.head else 'None'}")

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")

    def get_size(self):
        print(f"Current size: {self.size}")
        return self.size

    def prepend(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        print(f"Prepended {element} to the list")

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Print Linked list: [" + " ".join(elements) + "]")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.get(0)
    ll.set(0, 10)
    ll.get(0)
    ll.get_size()
    ll.prepend(10)
    ll.get(0)
    ll.print_list()

