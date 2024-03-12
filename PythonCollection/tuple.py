# Create a tuple
my_tuple = ("apple", "banana", "cherry", "apple")

# 1. Access an item by index
print("Second item:", my_tuple[1])  # Output: Second item: banana

# 2. Trying to modify will result in an error
# my_tuple[1] = "orange"  # This will raise a TypeError

# 3. Concatenating tuples
new_tuple = my_tuple + ("orange",)
print("Concatenated tuple:", new_tuple)  # Output: Concatenated tuple: ('apple', 'banana', 'cherry', 'apple', 'orange')

# 4. Duplicate members allowed
print("Tuple with duplicate member:", my_tuple)  # Output: Tuple with duplicate member: ('apple', 'banana', 'cherry', 'apple')
