# ============================================================
# 🧠 USER INPUT IN PYTHON
# ============================================================

# -----------------------------------------------
# 1️⃣ Basic Input
# -----------------------------------------------
# input() always returns data as a string.
name = input("Enter your name: ")
print("Hello,", name)

# Example:
# Enter your name: Vinay
# Output: Hello, Vinay


# -----------------------------------------------
# 2️⃣ Type Conversion (Casting)
# -----------------------------------------------
# Convert string input to integer or float explicitly
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("Age:", age, "Height:", height)

# Example:
# Enter your age: 25
# Enter your height in meters: 1.75
# Output: Age: 25 Height: 1.75


# -----------------------------------------------
# 3️⃣ Evaluating Expressions with eval()
# -----------------------------------------------
# eval() automatically detects and evaluates valid Python expressions.
num = eval(input("Enter a number or expression: "))
print("Result:", num)

# Example:
# Enter a number or expression: 5 + 10
# Output: Result: 15

# ⚠️ Important Note:
# eval() only works with VALID Python expressions.
# For example:
# Enter a number or expression: hjghj
# → NameError: name 'hjghj' is not defined
#
# Because Python assumes 'hjghj' is a variable name, not text.
# To make it valid, wrap it in quotes:
# Enter a number or expression: "hjghj"
# Output: hjghj
#
# 💡 If you want to accept any random text safely,
# simply use input() instead of eval().


# -----------------------------------------------
# 4️⃣ Multiple Inputs in One Line using .split()
# -----------------------------------------------
# .split() splits a string into a list based on spaces (default) or a custom delimiter.

# Example 1: Space-separated input
data = input("Enter three numbers separated by space: ").split()
print("List of inputs:", data)

# Convert all to integers
nums = [int(x) for x in data]
print("Numbers as integers:", nums)
print("Sum of numbers:", sum(nums))

# Example:
# Enter three numbers separated by space: 10 20 30
# Output:
# List of inputs: ['10', '20', '30']
# Numbers as integers: [10, 20, 30]
# Sum of numbers: 60

# Example 2: Comma-separated input
names = input("Enter names separated by commas: ").split(",")
print("Names list:", names)

# Example:
# Enter names separated by commas: Alice,Bob,Charlie
# Output: Names list: ['Alice', 'Bob', 'Charlie']


# -----------------------------------------------
# 5️⃣ Summary Notes
# -----------------------------------------------
# 🔹 input() → Always returns string.
# 🔹 int(), float(), bool() → Used for explicit type conversion.
# 🔹 eval() → Executes valid Python expressions (not random text).
# 🔹 .split() → Splits input string into list items.
# 🔹 Prefer plain input() for general user input to avoid eval() risks.
