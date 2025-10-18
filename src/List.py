# ===============================================
# Python Lists - Notes
# ===============================================

# -------------------------------
# 1️⃣ Introduction to Lists
# -------------------------------
# A list stores a series of items in a particular order.
# You can access items using an index or within a loop.
# Lists are:
# - Ordered: Items have a defined order.
# - Mutable: You can change their content after creation.
# - Versatile: Can contain integers, floats, strings, booleans, or even other lists.
# - Defined using square brackets []

# Example: Creating lists
bikes = ["trek", "readline", "giant"]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True, 3.14]

# Accessing elements
first_bike = bikes[0]              # First item
last_bike = bikes[len(bikes)-1]    # Last item using length
print(first_bike, last_bike)       # Output: trek giant

# -------------------------------
# 2️⃣ Modifying Lists
# -------------------------------
# Lists are mutable, so you can add, remove, or change elements

numbers = [1, 2, 3, 4]

# Change element
numbers[1] = 20
print(numbers)  # Output: [1, 20, 3, 4]

# Add element at the end
numbers.append(5)
print(numbers)  # Output: [1, 20, 3, 4, 5]

# Insert at a specific position
numbers.insert(2, 99)
print(numbers)  # Output: [1, 20, 99, 3, 4, 5]

# Remove element by value
numbers.remove(20)
print(numbers)  # Output: [1, 99, 3, 4, 5]

# Remove element by index
numbers.pop(2)
print(numbers)  # Output: [1, 99, 4, 5]

# Clear the whole list
numbers.clear()
print(numbers)  # Output: []

# -------------------------------
# 3️⃣ List Operations
# -------------------------------

a = [1, 2, 33]
b = [4, 5, 6]

# Concatenation
c = a + b
print(c)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
d = a * 3
print(d)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Check if element exists
print(2 in a)    # Output: True
print(10 in a)   # Output: False

# Length of a list
print(len(a))    # Output: 3

# -------------------------------
# 4️⃣ Looping Through a List
# -------------------------------
bikes = ["trek", "readline", "giant"]
for bike in bikes:
    print(bike)

# -------------------------------
# 5️⃣ Adding Items Dynamically
# -------------------------------
bikes = []
bikes.append("trek")
bikes.append("Honda")
bikes.append("bullet")
print(bikes)  # Output: ['trek', 'Honda', 'bullet']

# -------------------------------
# 6️⃣ Numerical Lists and Range
# -------------------------------
# Using range(start, end) → generates numbers from start to end-1

for x in range(1, 11):
    print(x**2)  # (** is the exponent operator) Squares numbers from 1 to 10

# ===============================================
# Traversing a String from End to Start Using Index
# ===============================================

# Suppose we have a string
text = "Python"

# Using positive indexing with len() to traverse backwards
# Syntax: range(start, stop, step)
# - start: last index → len(text) - 1
# - stop: before first index → -1 (because stop is exclusive)
# - step: -1 (move backwards)

for i in range(len(text) - 1, -1, -1):
    print(text[i])

# Output:
# n
# o
# h
# t
# y
# P


# ===============================================
# SLICING, COPYING & LIST COMPREHENSION IN PYTHON
# ===============================================

# -----------------------------------------------
# 1️⃣ LIST SLICING
# -----------------------------------------------
# Slicing allows you to access a subset of a list using:
# list[start:end:step]
# - start → starting index (included)
# - end → ending index (excluded)
# - step → how many indices to move forward after each element

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # [10, 20, 30] (start defaults to 0)
print(numbers[3:])      # [40, 50, 60, 70] (till end)
print(numbers[::2])     # [10, 30, 50, 70] (step of 2)
print(numbers[::-1])    # [70, 60, 50, 40, 30, 20, 10] (reversed)

# ✅ Slicing does not modify the original list.
# ✅ It returns a NEW list with selected elements.

# -----------------------------------------------
# 🔹 Understanding the "step" parameter
# -----------------------------------------------
# The step value defines how many indices to move after each element.
# It does NOT mean skip that many elements.

# Example:
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[::2])  # [10, 30, 50, 70]

# Step = 2 → move 2 indices forward → skip 1 element in between.
# Picks elements at index 0, 2, 4, 6.

# Summary:
# | Step | Meaning                   | Example | Result           |
# |-------|---------------------------|----------|------------------|
# | 1     | Take every element        | a[::1]  | [10,20,30,40]   |
# | 2     | Take every 2nd element    | a[::2]  | [10,30,50,70]   |
# | 3     | Take every 3rd element    | a[::3]  | [10,40,70]      |

# -----------------------------------------------
# 2️⃣ COPYING A LIST
# -----------------------------------------------
# Assigning one list to another copies only the reference, not the data.

a = [1, 2, 3]
b = a          # Both refer to the same list
b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
# ❗ Both change because a and b point to the same memory location.

# ✅ To make a true (shallow) copy:
a = [1, 2, 3]
b = a[:]           # Using slicing
b = list(a)        # Using list() constructor
b = a.copy()       # Using copy() method

# ✅ Deep Copy (for nested lists)
# When a list contains other lists, shallow copy only copies the outer list.
# Both lists still share the same inner list reference.

import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)   # Deep copy makes completely independent copy
b[2][0] = 999

print("a =", a)   # [1, 2, [3, 4]]
print("b =", b)   # [1, 2, [999, 4]]

# ⚙️ Summary Table
# | Copy Type | Method | Nested Objects Shared? | Independent? |
# |------------|--------|-----------------------|---------------|
# | Assignment | b = a | Yes | ❌ No |
# | Shallow Copy | a[:] / list(a) / a.copy() | Yes | ❌ No |
# | Deep Copy | copy.deepcopy(a) | No | ✅ Yes |

# -----------------------------------------------
# 3️⃣ LIST COMPREHENSION
# -----------------------------------------------
# A concise and Pythonic way to create lists using a single line.
# Syntax:
# [expression for item in iterable if condition]

# 🔸 Example 1: Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 🔸 Example 2: Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# 🔸 Example 3: Create a list of uppercase fruits
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# -----------------------------------------------
# 4️⃣ UNDERSTANDING LIST COMPREHENSION SYNTAX
# -----------------------------------------------
# General form:
# [ expression for item in iterable if condition ]

# ✅ Expression: what to store in the new list
# ✅ for item in iterable: loop through elements
# ✅ if condition: (optional) filter items

# 🔹 Equivalent traditional code:
squares = []
for x in range(1, 6):
    squares.append(x**2)

# 🔹 Example with condition:
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

# -----------------------------------------------
# 5️⃣ Inline if-else inside List Comprehension
# -----------------------------------------------
# You can also include condition inside the expression.

nums = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# -----------------------------------------------
# 6️⃣ Summary Table
# -----------------------------------------------
# | Type | Syntax | Example | Meaning |
# |------|---------|----------|----------|
# | Simple | [expr for x in iterable] | [x**2 for x in range(5)] | Squares |
# | With condition | [expr for x in iterable if cond] | [x for x in range(10) if x%2==0] | Filter evens |
# | Inline if-else | [A if cond else B for x in iterable] | ["Even" if x%2==0 else "Odd" for x in range(5)] | Label even/odd |

# ✅ List comprehensions are more readable, faster, and concise.


# -------------------------------
# ✅ Summary
# -------------------------------
# 1. Lists store multiple items in an ordered collection.
# 2. You can access elements using indexing or loops.
# 3. Lists are mutable: elements can be changed, added, or removed.
# 4. Common operations: append, insert, remove, pop, clear, concatenation, repetition.
# 5. Looping and range help generate sequences and perform calculations.


# ===============================================
# Summary: Python Lists vs Java Arrays / ArrayList
# ===============================================

# 1️⃣ Python Lists
# - Python lists are **dynamic and mutable** by default.
# - You can add, remove, or modify elements at any time.
# - Lists can store **mixed data types**: integers, strings, floats, booleans, or even other lists.
# - No need to declare a fixed size in advance.
# - Internally, Python lists are implemented as dynamic arrays (resize automatically).

# Example:
numbers = [1, 2, 3]   # list with 3 elements
numbers.append(4)      # add new element
print(numbers)         # Output: [1, 2, 3, 4]

# Python does not have a native static array like Java.
# If a fixed-size, homogeneous array is needed, use:
import array
arr = array.array('i', [1, 2, 3])  # array of integers
arr.append(4)                       # still allows dynamic resizing
print(arr)                          # Output: array('i', [1, 2, 3, 4])

# -------------------------------
# 2️⃣ Comparison with Java
# -------------------------------

# | Feature                | Java Array           | Java ArrayList         | Python List            |
# |------------------------|--------------------|----------------------|-----------------------|
# | Size                   | Fixed (Static)     | Dynamic (Resizable)  | Dynamic (Resizable)   |
# | Type                   | Homogeneous        | Homogeneous (ideally)| Mixed allowed         |
# | Add/Remove elements    | Not allowed        | Allowed              | Allowed               |
# | Syntax                 | int[] arr = new int[5]; | ArrayList<Integer> arr = new ArrayList<>(); | arr = [1, 2, 3] |
# | Memory Allocation      | Contiguous block   | Internal resizing    | Internal resizing     |

# ✅ Key Takeaways
# 1. Python lists are flexible and dynamic; you rarely need a separate dynamic array type.
# 2. No native static arrays exist in Python like in Java.
# 3. Use `array.array` or NumPy arrays for fixed-type numeric arrays.


# ===============================================
# Type Safety and Generics: Python vs Java
# ===============================================

# 1️⃣ Java Lists with Generics
# - Java enforces type safety at **compile time** using Generics.
# - Example: Only integers can be added to a List<Integer>
# - Compiler prevents mixing types.

# Java Example:
# ArrayList<Integer> numbers = new ArrayList<>();
# numbers.add(10)      # ✅ OK
# numbers.add("Hello") # ❌ Compile-time error

# -------------------------------
# 2️⃣ Python Lists
# - Python lists are **dynamic and flexible**.
# - They can store elements of **any type**:
my_list = [1, "hello", True, 3.14]  # ✅ Allowed

# - Python enforces **type rules at runtime** when performing operations:
x = 10
y = "5"

# print(x + y)  # ❌ TypeError at runtime

# Example of valid operation:
print(my_list[0] + my_list[2])  # 1 + True = 2

# Example of invalid operation:
# print(my_list[0] + my_list[1])  # ❌ TypeError

# -------------------------------
# 3️⃣ Type Hints (Optional: Python Generics)
# - Python does not have compile-time generics like Java.
# - Use `typing` module for **type hints** to help developers/IDEs:

from typing import List

numbers: List[int] = [1, 2, 3]
numbers.append(4)  # ✅ OK
# numbers.append("hello")  # IDE warning, runtime still allows it

# -------------------------------
# 4️⃣ Comparison Table

# | Feature                  | Java (Generics)              | Python (List)                  |
# |---------------------------|-----------------------------|--------------------------------|
# | Type Safety               | Compile-time enforced       | Runtime enforced (strong typing) |
# | Can store mixed types     | ❌ Only declared type       | ✅ Allowed                      |
# | Compiler/runtime check    | Compiler                    | Runtime (TypeError on invalid operations) |
# | Generic-like hints        | Generics enforce type       | typing.List[int] hints (optional) |

# -------------------------------
# ✅ Key Takeaways
# 1. Python lists are flexible and can store mixed types.
# 2. Python is type-safe at operation level but not at container level.
# 3. Type hints can mimic generics for **documentation and static analysis**.
# 4. Java enforces type safety at compile time using generics.