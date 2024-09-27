from my_class import MyClass  # Import the class from the separate file

# Create instances
def create_instances(num_instances):
    instances = []
    for _ in range(num_instances):
        instance = MyClass()  # Create instance with hardcoded attributes
        instances.append(instance)
    return instances

# Function to calculate total allocated memory for all instances
def calculate_total_memory(instances):
    total_memory = 0
    for instance in instances:
        total_memory += instance.calculate_memory()  # Use the class method
    return total_memory

# Number of instances to create
num_instances = 100

# Create instances
instances = create_instances(num_instances)

# Calculate total memory
total_memory = calculate_total_memory(instances)

print(f"Total memory allocated for {num_instances} instances: {total_memory} bytes")