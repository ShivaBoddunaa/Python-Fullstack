# 1. Function to check if a string is palindrome
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("Madam"))
print(is_palindrome("Hello"))


# 2. Function to find sum of digits of a number
def sum_of_digits(num):
    return sum(int(d) for d in str(num))

print(sum_of_digits(12345))
print(sum_of_digits(907))


# 3. Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4]))
print(remove_duplicates(["a", "b", "a", "c"]))


# 4. Function to return Fibonacci series of length n
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series

print(fibonacci(5))
print(fibonacci(10))
