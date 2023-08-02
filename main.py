# Variable declaration and assignment
name = "John"
age = 25
is_student = True

# Math operations
a = 10
b = 5

# Addition
result_add = a + b
print("Addition:", result_add)  # Output: 15

# Subtraction
result_sub = a - b
print("Subtraction:", result_sub)  # Output: 5

# Multiplication
result_mul = a * b
print("Multiplication:", result_mul)  # Output: 50

# Division
try:
    result_div = a / b
    print("Division:", result_div)  # Output: 2.0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Arrays (lists)
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)

# Dictionaries (key-value pairs)
person = {"name": "John", "age": 25, "is_student": True}
print("Person:", person)

# Operations in arrays
fruits.append("grape")
print("Updated Fruits:", fruits)

# Operations in dictionaries
person["location"] = "New York"
print("Updated Person:", person)

# If statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For each loop (using for loop)
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Opening a file using context manager
filename = "example.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File Content:", content)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Print statements
print("Name:", name, "Age:", age)

# String interpolation using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
