"""
Python Basics - Beginner Practice Exercises
============================================
Simple exercises to learn Python fundamentals.
Complete each TODO and run the file to check your work!
"""

print("Welcome to Python Basics Practice!\n")
print("=" * 50)

# ============================================================================
# EXERCISE 1: Variables and Data Types
# ============================================================================
print("\nEXERCISE 1: Variables")
print("-" * 50)

# TODO: Create a variable called 'my_name' with your name
my_name =input("enter your name")

# TODO: Create a variable called 'my_age' with your age
my_age = int(input("enter your age"))

# TODO: Create a variable called 'my_height' with your height in meters
my_height = int(input("enter your height"))

print(f"My name is {my_name}")
print(f"I am {my_age} years old")
print(f"I am {my_height}m tall")

# ============================================================================
# EXERCISE 2: Basic Math Operations
# ============================================================================
print("\n\nEXERCISE 2: Math Operations")
print("-" * 50)

# TODO: Calculate the sum of 15 and 27
a = int(input("enter your value "))
b = int(input("enter your value "))


# TODO: Calculate 10 multiplied by 5
a = int(input("enter your value "))
b = int(input("enter your value "))

# TODO: Calculate 100 divided by 4
a = int(input("enter your value "))
b = int(input("enter your value "))

print(f"a + b = {a+b}")
print(f"a × b = {a*b}")
print(f"a ÷ b = {a % b}")

# ============================================================================
# EXERCISE 3: Strings
# ============================================================================
print("\n\nEXERCISE 3: Working with Strings")
print("-" * 50)

# TODO: Create a variable with your favorite food
favorite_food = input("Enter your Fav Food ")

# TODO: Create a variable with your favorite color
favorite_color =input("Enter your Fav colour")

# TODO: Combine them into a sentence
sentence = f"I like {favorite_color} and I love eating {favorite_food}!"

print(sentence)
print(f"The sentence has {len(sentence)} characters")

# ============================================================================
# EXERCISE 4: Lists
# ============================================================================
print("\n\nEXERCISE 4: Lists")
print("-" * 50)

# TODO: Create a list of your 3 favorite fruits
fruits = ["apple", "banana", "mango"]

# TODO: Add one more fruit to the list
fruits.append("orange")

# TODO: Print the first fruit
first_fruit = fruits[0]

print(f"My fruits: {fruits}")
print(f"First fruit: {first_fruit}")
print(f"Total fruits: {len(fruits)}")

# ============================================================================
# EXERCISE 5: Conditional Statements (if/else)
# ============================================================================
print("\n\nEXERCISE 5: If/Else Statements")
print("-" * 50)

# TODO: Create a variable called 'temperature' 
temperature = 25

# TODO: Write if/else to print "Hot" if temp > 30, otherwise "Nice"
if temperature > 30:
    print(f"Temperature is {temperature}°C - It's hot!")
else:
    print(f"Temperature is {temperature}°C - Nice weather!")

# TODO: Create a variable called 'score'
score = 85

# TODO: Print grade based on score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} - Grade: {grade}")

# ============================================================================
# EXERCISE 6: Loops - For Loop
# ============================================================================
print("\n\nEXERCISE 6: For Loops")
print("-" * 50)

# TODO: Use a for loop to print numbers 1 to 5
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# TODO: Loop through a list of colors and print each one
colors = ["red", "green", "blue", "yellow"]
print("\nColors:")
for color in colors:
    print(f"- {color}")

# ============================================================================
# EXERCISE 7: Loops - While Loop
# ============================================================================
print("\n\nEXERCISE 7: While Loops")
print("-" * 50)

# TODO: Use while loop to count down from 5 to 1
countdown = 5
print("Countdown:")
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("Blast off!")

# ============================================================================
# EXERCISE 8: Dictionaries
# ============================================================================
print("\n\nEXERCISE 8: Dictionaries")
print("-" * 50)

# TODO: Create a dictionary with your info (name, age, city)
my_info = {
    "name": "Student",
    "age": 20,
    "city": "Mumbai"
}

# TODO: Add a new key "hobby" to the dictionary
my_info["hobby"] = "coding"

# TODO: Print each key-value pair
print("My Information:")
for key, value in my_info.items():
    print(f"{key}: {value}")

# ============================================================================
# EXERCISE 9: Simple Function
# ============================================================================
print("\n\nEXERCISE 9: Functions")
print("-" * 50)

# TODO: Write a function that takes a name and returns a greeting
def greet_person(name):
    return f"Hello, {name}! Welcome to Python!"

# Test the function
greeting1 = greet_person("Alice")
greeting2 = greet_person("Bob")

print(greeting1)
print(greeting2)

# TODO: Write a function that adds two numbers
def add_numbers(a, b):
    return a + b

# Test the function
result1 = add_numbers(10, 5)
result2 = add_numbers(100, 250)

print(f"\n10 + 5 = {result1}")
print(f"100 + 250 = {result2}")

# ============================================================================
# EXERCISE 10: Mini Project - Even or Odd Checker
# ============================================================================
print("\n\nEXERCISE 10: Mini Project")
print("-" * 50)

# TODO: Write a function that checks if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Test with different numbers
test_numbers = [2, 7, 10, 15, 20]

print("Even or Odd Checker:")
for num in test_numbers:
    result = check_even_odd(num)
    print(f"{num} is {result}")

# ============================================================================
# BONUS: Try These Challenges!
# ============================================================================
print("\n\n" + "=" * 50)
print("BONUS CHALLENGES - Try these on your own!")
print("=" * 50)

# CHALLENGE 1: Write a function to find the largest number in a list
def find_largest(numbers):
    # TODO: Your code here
    pass

# CHALLENGE 2: Write a function to count how many times a word appears
def count_word(sentence, word):
    # TODO: Your code here
    pass

# CHALLENGE 3: Write a function to reverse a string
def reverse_string(text):
    # TODO: Your code here
    pass

# Uncomment these to test your bonus challenges:
# print(find_largest([3, 7, 2, 9, 1]))  # Should print 9
# print(count_word("hello world hello", "hello"))  # Should print 2
# print(reverse_string("Python"))  # Should print "nohtyP"

print("\n✅ All exercises completed!")
print("Now try the bonus challenges above!")
print("=" * 50)