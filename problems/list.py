# ==================== LIST PROBLEMS ====================

print("=" * 60)
print("LIST PROBLEMS")
print("=" * 60)

# Problem 1: Find the largest and smallest number in a list
print("\n1. Find largest and smallest number in a list")
print("-" * 60)

numbers = [45, 12, 78, 34, 89, 23, 67]
print(f"List: {numbers}")

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

# Alternative using built-in functions
print(f"Largest (using max): {max(numbers)}")
print(f"Smallest (using min): {min(numbers)}")


# Problem 2: Remove duplicates from a list
print("\n2. Remove duplicates from a list")
print("-" * 60)

numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print(f"Original list: {numbers_with_duplicates}")

# Method 1: Using loop
unique_list = []
for num in numbers_with_duplicates:
    if num not in unique_list:
        unique_list.append(num)

print(f"Without duplicates (method 1): {unique_list}")

# Method 2: Using set (loses order)
unique_list2 = list(set(numbers_with_duplicates))
print(f"Without duplicates (method 2): {unique_list2}")


# Problem 3: Find common elements between two lists
print("\n3. Find common elements between two lists")
print("-" * 60)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Method 1: Using loop
common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print(f"Common elements (method 1): {common}")

# Method 2: Using list comprehension
common2 = [item for item in list1 if item in list2]
print(f"Common elements (method 2): {common2}")

# Method 3: Using set intersection
common3 = list(set(list1) & set(list2))
print(f"Common elements (method 3): {common3}")