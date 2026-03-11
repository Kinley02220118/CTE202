class CustomList:
    def __init__(self, capacity=10):
        self.data = [None] * capacity   # storage
        self.capacity = capacity        # max size
        self.size = 0                   # current number of elements
        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.size)

    def append(self, element):
        if self.size < self.capacity:
            self.data[self.size] = element
            self.size += 1
            print("Appended", element, "to the list")
        else:
            print("List is full, cannot append")

    def get(self, index):
        if 0 <= index < self.size:
            print("Element at index", index, ":", self.data[index])
            return self.data[index]
        else:
            print("Index out of bounds")

    def set(self, index, element):
        if 0 <= index < self.size:
            self.data[index] = element
            print("Set element at index", index, "to", element)
        else:
            print("Index out of bounds")

    def size_of_list(self):
        print("Current size:", self.size)
        return self.size

lst = CustomList()
lst.append(5)          # Appended 5 to the list
lst.get(0)             # Element at index 0: 5
lst.set(0, 10)         # Set element at index 0 to 10
lst.get(0)             # Element at index 0: 10
lst.size_of_list()