# Task 1: Implementthe List Class Structure
# Create a class called CustomList that uses an underlying array for storage. Your
# implementation should include:
# ● Private array to store elements
# ● Variables to track capacity and current size
# ● Constructor that initializes the array with a default capacity
# Example Output:
# Created new CustomList with capacity: 10
# Current size: 0

class CustomList:
    def __init__(self, capacity=10):
        # Variable to track capacity
        self._capacity = capacity  # Default capacity of the list
        
        # Variable to track current size
        self._size = 0  # Number of elements currently in the list
        
        # Private array to store elements
        self._array = [None] * self._capacity  # List storage initialized with None values
        
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")


custom_list = CustomList()


# TASK2
# TASK2
class CustomList:
    def __init__(self, capacity=10):
        """Constructor to initialize the CustomList with a given capacity (default is 10)."""
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
       
    
    def append(self, element):
        """Append an element to the end of the list."""
        if self.size == self.capacity:
            self._resize()  # Resize the array if capacity is reached
        self.array[self.size] = element
        self.size += 1
        print(f"Appended {element} to the list")
    
    def get(self, index):
        """Retrieve an element at a specific index."""
        if 0 <= index < self.size:
            return self.array[index]
        else:
            return "Index out of bounds"
    
    def set(self, index, element):
        """Replace an element at a specific index."""
        if 0 <= index < self.size:
            self.array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of bounds")
    
    def size(self):
        """Return the current number of elements."""
        return self.size
    
    def _resize(self):
        """Resize the array when capacity is reached."""
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        print(f"Resized list to new capacity: {self.capacity}")

# Example usage:
custom_list = CustomList()  # Creates a list with default capacity of 10
custom_list.append(5)
custom_list.append(7)
print(f"Element at index 1: {custom_list.get(1)}")
custom_list.set(0, 10)
print(f"Element at index 0: {custom_list.get(0)}")
print(f"Current size: {custom_list.size}")
