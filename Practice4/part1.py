# 1. Function to check if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(check_even_odd(10))
print(check_even_odd(7))


# 2. Function to find factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))
print(factorial(7))


# 3. Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

print(count_vowels("Hello World"))
print(count_vowels("Python"))


# 4. Function to return the largest of three numbers
def largest(a, b, c):
    return max(a, b, c)

print(largest(10, 25, 15))
print(largest(100, 99, 101))
