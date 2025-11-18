# ----------------------------
# PYTHON PRACTICE – PART 2
# SET & DICTIONARY PROBLEMS
# ----------------------------

# 6. Find common elements between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common = set1.intersection(set2)
print("Common elements:", common)

# 7. Check if a set is subset of another
a = {1, 2}
b = {1, 2, 3, 4}
print("Is subset?:", a.issubset(b))

# 8. Count character frequency in a string
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("Character frequency:", freq)

# 9. Find key with maximum value in dictionary
scores = {"a": 10, "b": 50, "c": 30}
max_key = max(scores, key=scores.get)
print("Key with max value:", max_key)

# 10. Swap keys and values in dictionary
d = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in d.items()}
print("Swapped dictionary:", swapped)
