# ===============================================
# TUPLE IN PYTHON
# ===============================================

# -----------------------------------------------
# 1️⃣ What is a Tuple?
# -----------------------------------------------
# A Tuple is an ordered, immutable collection of elements in Python.
# It is similar to a list, but once created, its elements cannot be modified.

# ✅ Key Features:
# - Ordered (elements maintain their sequence)
# - Immutable (cannot add, remove, or change elements)
# - Allows duplicate values
# - Can contain elements of different data types

# -----------------------------------------------
# 2️⃣ Creating Tuples
# -----------------------------------------------
# Using parentheses
t1 = (10, 20, 30)

# Tuple with mixed data types
t2 = (10, "Python", 3.14)

# Tuple without parentheses (tuple packing)
t3 = 10, 20, 30

# Single element tuple (comma is must)
t4 = (10,)
print(type(t4))  # <class 'tuple'>

# Without comma → just an integer
t5 = (10)
print(type(t5))  # <class 'int'>

# -----------------------------------------------
# 3️⃣ Accessing Elements
# -----------------------------------------------
t = (10, 20, 30, 40, 50)

print(t[0])      # First element: 10
print(t[-1])     # Last element: 50
print(t[1:4])    # Slice: (20, 30, 40)

# -----------------------------------------------
# 4️⃣ Tuple Operations
# -----------------------------------------------
a = (1, 2, 3)
b = (4, 5, 6)

# Concatenation
c = a + b
print(c)  # (1, 2, 3, 4, 5, 6)

# Repetition
d = a * 2
print(d)  # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in a)    # True
print(10 in a)   # False

# Length
print(len(a))    # 3

# -----------------------------------------------
# 5️⃣ Immutability
# -----------------------------------------------
t = (10, 20, 30)
# t[1] = 100  # ❌ TypeError: 'tuple' object does not support item assignment

# However, if a tuple contains a mutable object (like a list):
t = (1, [2, 3], 4)
t[1][0] = 100
print(t)  # (1, [100, 3], 4)

# -----------------------------------------------
# 6️⃣ Tuple Packing & Unpacking
# -----------------------------------------------
# Packing
t = 10, 20, 30

# Unpacking
a, b, c = t
print(a, b, c)  # 10 20 30

# Using * to capture remaining elements
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]

# -----------------------------------------------
# 7️⃣ Tuple Methods
# -----------------------------------------------
t = (1, 2, 2, 3)

print(t.count(2))  # 2 → counts occurrences of 2
print(t.index(3))  # 3 → index of first occurrence of 3

# -----------------------------------------------
# 8️⃣ Tuple as Immutable List
# -----------------------------------------------
# Use tuple when you need an immutable collection
# e.g., fixed data, constant values, dictionary keys, coordinates

# Conversion
my_list = [1, 2, 3]
immutable = tuple(my_list)  # List → Tuple

mutable = list(immutable)   # Tuple → List

# -----------------------------------------------
# 9️⃣ Comparison Between List and Tuple
# -----------------------------------------------
# | Feature | List | Tuple |
# |---------|------|-------|
# | Syntax | [] | () |
# | Mutability | Mutable | Immutable |
# | Performance | Slower | Faster |
# | Can be dict key | ❌ No | ✅ Yes |
# | Methods | Many (`append`, `remove`) | Few (`count`, `index`) |

# -----------------------------------------------
# 10️⃣ Example Program
# -----------------------------------------------
person = ("Vinay", 28, "Developer")

# Accessing elements
print(person[0])  # Vinay

# Unpacking
name, age, role = person
print(f"Name: {name}, Age: {age}, Role: {role}")

# Trying to modify (will cause error)
# person[1] = 29  # ❌ TypeError
