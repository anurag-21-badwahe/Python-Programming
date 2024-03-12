'''.
List is a collection which is ordered and changeable. Allows duplicate members.
'''

# Create a list
my_list = ["apple", "banana", "cherry", "apple"]

# 1. Access an item by index
print("First item:", my_list[0])  # Output: First item: apple

# 2. Modify an item
my_list[1] = "orange"
print("Modified list:", my_list)  # Output: Modified list: ['apple', 'orange', 'cherry', 'apple']

# 3. Append an item
my_list.append("grape")
print("Appended list:", my_list)  # Output: Appended list: ['apple', 'orange', 'cherry', 'apple', 'grape']

# 4. Remove an item
my_list.remove("cherry")
print("List after removal:", my_list)  # Output: List after removal: ['apple', 'orange', 'apple', 'grape']

# 5. Duplicate members allowed
my_list.append("orange")
print("List with duplicate member:", my_list)  # Output: List with duplicate member: ['apple', 'orange', 'apple', 'grape', 'orange']
