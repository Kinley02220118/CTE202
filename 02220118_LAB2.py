# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("Created new LinkedList")
        print("Current size:", self._size)
        print("Head:", self.head)

    # Append element to the end
    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"Appended {element} to the list")

    # Get element at index
    def get(self, index):
        if index < 0 or index >= self._size:
            return "Index out of range"

        current = self.head
        for i in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    # Set element at index
    def set(self, index, element):
        if index < 0 or index >= self._size:
            return "Index out of range"

        current = self.head
        for i in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    # Return size
    def size(self):
        print("Current size:", self._size)
        return self._size

    # Prepend element to the beginning
    def prepend(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1
        print(f"Prepend {element} to the list")

    # Print linked list
    def print_list(self):
        current = self.head
        print("Print Linked list :[", end="")

        while current:
            print(current.data, end=" ")
            current = current.next

        print("]")


# -------------------------
# Example Usage
# -------------------------
ll = LinkedList()

ll.append(5)
ll.get(0)

ll.set(0, 10)
ll.get(0)

ll.size()

ll.prepend(10)
ll.print_list()