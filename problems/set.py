# ==================== SET PROBLEMS ====================

print("\n\n" + "=" * 60)
print("SET PROBLEMS")
print("=" * 60)

# Problem 1: Union and Intersection of two sets
print("\n1. Union and Intersection of two sets")
print("-" * 60)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union - all unique elements from both sets
union_set = set1 | set2
print(f"Union (set1 | set2): {union_set}")
print(f"Union (using union()): {set1.union(set2)}")

# Intersection - common elements
intersection_set = set1 & set2
print(f"Intersection (set1 & set2): {intersection_set}")
print(f"Intersection (using intersection()): {set1.intersection(set2)}")


# Problem 2: Difference between two sets
print("\n2. Difference between two sets")
print("-" * 60)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Elements in A but not in B
difference1 = set_a - set_b
print(f"A - B (in A but not in B): {difference1}")

# Elements in B but not in A
difference2 = set_b - set_a
print(f"B - A (in B but not in A): {difference2}")

# Symmetric difference - elements in either but not both
symmetric_diff = set_a ^ set_b
print(f"Symmetric difference (A ^ B): {symmetric_diff}")


# Problem 3: Check if one set is subset/superset of another
print("\n3. Check if one set is subset/superset")
print("-" * 60)

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")

# Check if X is subset of Y
is_subset = set_x.issubset(set_y)
print(f"Is X subset of Y? {is_subset}")

# Check if Y is superset of X
is_superset = set_y.issuperset(set_x)
print(f"Is Y superset of X? {is_superset}")

# Manual check for subset
all_in_y = True
for item in set_x:
    if item not in set_y:
        all_in_y = False
        break

print(f"Manual check - X subset of Y? {all_in_y}")


print("\n" + "=" * 60)
print("All problems completed!")
print("=" * 60)