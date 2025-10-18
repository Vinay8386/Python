# ===============================================
# Python Operators - Teaching Notes
# ===============================================

# Operators in Python are special symbols used to perform operations on variables and values.
# Python supports several types of operators: arithmetic, comparison, assignment, logical, identity, membership, and bitwise.

# -------------------------------
# 1️⃣ Arithmetic Operators
# -------------------------------
# Used for mathematical calculations.

a = 10
b = 3

print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.3333
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)        # 1
print("Exponentiation:", a ** b) # 1000

# -------------------------------
# 2️⃣ Comparison Operators
# -------------------------------
# Compare values and return True or False.

x = 10
y = 20

print("Equal:", x == y)        # False
print("Not equal:", x != y)    # True
print("Greater than:", x > y)  # False
print("Less than:", x < y)     # True
print("Greater or equal:", x >= 10) # True
print("Less or equal:", y <= 15)    # False

# -------------------------------
# 3️⃣ Assignment Operators
# -------------------------------
# Assign values to variables or update them with operations.

x = 5
x += 3  # x = x + 3
print("x += 3:", x)  # 8

y = 10
y **= 2  # y = y ** 2
print("y **= 2:", y)  # 100

# Other assignment operators: -=, *=, /=, //=, %=

# -------------------------------
# 4️⃣ Logical Operators
# -------------------------------
# Combine Boolean expressions.

a = True
b = False

print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False

# -------------------------------
# 5️⃣ Identity Operators
# -------------------------------
# Check if two variables refer to the same object.

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is z:", x is z)       # True
print("x is y:", x is y)       # False
print("x is not y:", x is not y) # True

# -------------------------------
# 6️⃣ Membership Operators
# -------------------------------
# Check if a value exists in a sequence (list, string, tuple, etc.)

fruits = ["apple", "banana", "cherry"]

print("apple in fruits:", "apple" in fruits)      # True
print("mango not in fruits:", "mango" not in fruits)  # True

# -------------------------------
# 7️⃣ Bitwise Operators (Optional)
# -------------------------------
# Operate on binary representations of numbers.

a = 5  # 0b0101
b = 3  # 0b0011

print("a & b:", a & b)   # AND → 1 (0b0001)
print("a | b:", a | b)   # OR → 7 (0b0111)
print("a ^ b:", a ^ b)   # XOR → 6 (0b0110)
print("~a:", ~a)         # NOT → -6
print("a << 1:", a << 1) # Left shift → 10
print("a >> 1:", a >> 1) # Right shift → 2

# -------------------------------
# ✅ Summary
# -------------------------------
# 1. Arithmetic → +, -, *, /, %, **, //
# 2. Comparison → ==, !=, >, <, >=, <=
# 3. Assignment → =, +=, -=, *=, /=, //=, %=, **=
# 4. Logical → and, or, not
# 5. Identity → is, is not
# 6. Membership → in, not in
# 7. Bitwise → &, |, ^, ~, <<, >>
