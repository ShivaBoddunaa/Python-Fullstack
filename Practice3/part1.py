# ----------------------------
# PYTHON PRACTICE – PART 1
# LIST & TUPLE PROBLEMS
# ----------------------------

# 1. Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique list:", unique_numbers)

# 2. Find largest and smallest number in a list
nums = [10, 5, 7, 25, 1]
print("Largest:", max(nums))
print("Smallest:", min(nums))

# 3. Reverse a list without using reverse()
items = [1, 2, 3, 4, 5]
reversed_list = items[::-1]
print("Reversed list:", reversed_list)

# 4. Count occurrences of an element in a tuple
t = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", t.count(2))

# 5. Convert tuple → list → tuple (add new element)
t2 = (10, 20, 30)
lst = list(t2)
lst.append(40)
t2_new = tuple(lst)
print("Updated tuple:", t2_new)
