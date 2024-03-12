# Create a set
my_set = {"apple", "banana", "cherry"}

# 1. Trying to access by index will result in an error because sets are unordered and unindexed
# print(my_set[0])  # This will raise a TypeError

# 2. Trying to modify an item will result in an error because sets are unchangeable
# my_set.add("orange")  # This will raise an AttributeError

# 3. Adding items to a set
my_set.add("orange")
print("Set after addition:", my_set)  # Output: Set after addition: {'banana', 'cherry', 'orange', 'apple'}

# 4. Duplicate members not allowed
my_set.add("apple")  # Adding a duplicate member
print("Set with duplicate member:", my_set)  # Output: Set with duplicate member: {'banana', 'cherry', 'orange', 'apple'}
