# Create a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# 1. Accessing value by key
print("Age:", my_dict["age"])  # Output: Age: 30

# 2. Modifying value by key
my_dict["age"] = 35
print("Updated age:", my_dict)  # Output: Updated age: {'name': 'John', 'age': 35, 'city': 'New York'}

# 3. Adding new key-value pairs
my_dict["country"] = "USA"
print("Dictionary after addition:", my_dict)  # Output: Dictionary after addition: {'name': 'John', 'age': 35, 'city': 'New York', 'country': 'USA'}

# 4. Keys must be unique, so updating a key will replace its value
my_dict["name"] = "Mike"
print("Updated dictionary:", my_dict)  # Output: Updated dictionary: {'name': 'Mike', 'age': 35, 'city': 'New York', 'country': 'USA'}
