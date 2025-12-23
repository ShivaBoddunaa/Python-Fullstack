
print("\n\n" + "=" * 60)
print("TUPLE PROBLEMS")
print("=" * 60)

# Problem 1: Count occurrences of an element in tuple
print("\n1. Count occurrences of an element in tuple")
print("-" * 60)

my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
print(f"Tuple: {my_tuple}")

element = 2
count = 0

for item in my_tuple:
    if item == element:
        count += 1

print(f"Element {element} appears {count} times")

# Using built-in method
print(f"Using count(): {my_tuple.count(element)} times")


# Problem 2: Find maximum and minimum in a tuple
print("\n2. Find maximum and minimum in a tuple")
print("-" * 60)

numbers_tuple = (45, 12, 78, 34, 89, 23, 67)
print(f"Tuple: {numbers_tuple}")

# Method 1: Using loop
max_num = numbers_tuple[0]
min_num = numbers_tuple[0]

for num in numbers_tuple:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")

# Method 2: Using built-in functions
print(f"Maximum (using max): {max(numbers_tuple)}")
print(f"Minimum (using min): {min(numbers_tuple)}")


# Problem 3: Convert tuple of tuples to list of lists
print("\n3. Convert tuple of tuples to list of lists")
print("-" * 60)

tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Tuple of tuples: {tuple_of_tuples}")

# Method 1: Using loop
list_of_lists = []
for inner_tuple in tuple_of_tuples:
    list_of_lists.append(list(inner_tuple))

print(f"List of lists (method 1): {list_of_lists}")

# Method 2: Using list comprehension
list_of_lists2 = [list(inner) for inner in tuple_of_tuples]
print(f"List of lists (method 2): {list_of_lists2}")