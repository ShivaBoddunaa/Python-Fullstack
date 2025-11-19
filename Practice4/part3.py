# 1. Higher-order function: apply a function to all elements of a list
def apply_function(func, data):
    return [func(x) for x in data]

def square(n): return n*n
def cube(n): return n*n*n

print(apply_function(square, [1, 2, 3, 4]))
print(apply_function(cube, [2, 3, 4]))


# 2. Function returning another function (closure)
def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(7))


# 3. Function with variable-length arguments (*args)
def avg(*nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

print(avg(10, 20, 30))
print(avg(5, 15, 25, 35, 45))


# 4. Lambda + sorting complex structure
students = [
    ("Shiva", 85),
    ("Aarav", 91),
    ("Kiran", 78),
]

# sort by marks using lambda
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)


# 5. Recursion: sum of list
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([1, 2, 3, 4, 5]))
print(recursive_sum([10, 20, 30]))


# 6. Decorator to measure time taken by a function
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())


# 7. Using map, filter, reduce
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda a, b: a + b, nums)

print(squared)
print(evens)
print(total)


# 8. Function to flatten a nested list (advanced recursion)
def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

print(flatten_list([1, [2, 3], [4, [5, 6]]]))
