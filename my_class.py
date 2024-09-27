import sys

class MyClass:
    def __init__(self):
        # Hardcoded attributes, we add here all the things
        self.int_val = 10
        self.float_val = 20.5
        self.str_val = "Hello, world!"
        self.list_val = [1, 2, 3, 4, 5]

    # Method to calculate the memory of the instance and its attributes
    def calculate_memory(self):
        total_memory = sys.getsizeof(self)  # Memory of the instance itself
        
        # Memory of individual attributes
        total_memory += sys.getsizeof(self.int_val)
        total_memory += sys.getsizeof(self.float_val)
        total_memory += sys.getsizeof(self.str_val)
        total_memory += sys.getsizeof(self.list_val)
        
        return total_memory