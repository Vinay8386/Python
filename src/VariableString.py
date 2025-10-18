# ===============================================
# Python Variables and Strings - Notes
# ===============================================

# -------------------------------
# 1️⃣ Printing Output
# -------------------------------
# The simplest way to display information in Python is using the print() function
print("Hello World")  # Output: Hello World

# -------------------------------
# 2️⃣ Variables in Python
# -------------------------------
# A variable is like a container that stores data.
# In Python, you don’t need to declare its type explicitly — Python figures it out automatically (dynamic typing).
# Variables are used to assign labels to values.

# Assigning string values to variables
f_name = "Vinay"
l_name = "Mishra"

# Concatenating variables to form full name
full_name = f_name + " " + l_name
print(full_name)  # Output: Vinay Mishra

# -------------------------------
# 3️⃣ Assigning Different Types of Values
# -------------------------------
# Integer
age = 25

# Float
height = 5.9

# String
name = "Vinay"

# Boolean
is_student = True

# -------------------------------
# 4️⃣ Multiple Assignment
# -------------------------------
# Assigning multiple variables at once
name, age = "Vinay", 25

print(name)  # Output: Vinay
print(age)   # Output: 25

# -------------------------------
# 5️⃣ Strings in Python
# -------------------------------
# A string is a sequence of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' or """ """).
# Triple quotes are used for multi-line strings.

# Single and double quotes
str1 = 'Hello'
str2 = "World"

# Triple quotes for multi-line string
str3 = """This is
a multi-line
string."""

print(str1, str2)  # Output: Hello World
print(str3)
# Output:
# This is
# a multi-line
# string.

# -------------------------------
# 6️⃣ String Operations
# -------------------------------
# Concatenation (joining strings)
greeting = "String" + " " + "Concatenation"
print(greeting)  # Output: String Concatenation

# Repetition
laugh = "Ha" * 3 #The * operator, when used with a string, repeats the string multiple times.
print(laugh)     # Output: HaHaHa

# Length of string
print(len(laugh))  # Output: 6

# Accessing characters
text = "Python"
print(text[0])       # First character: P
print(text[-1])      # Last character: n Accesses the last element directly using negative indexing
print(text[len(text)-1])  # Last character using length: n Calculates the index position manually:
print(text[1:4])     # Slicing (1 to 3): yth

#text[-1] → gives the value directly.
#len(text) - 1 → gives the index number.
#text[len(text) - 1] → gives the value, but less elegant than using text[-1].

# -------------------------------
# 7️⃣ String Methods
# -------------------------------
s = "python Programming"

print(s.upper())      # Convert to uppercase: PYTHON PROGRAMMING
print(s.lower())      # Convert to lowercase: python programming
print(s.capitalize()) # Capitalize first letter: Python programming
print(s.title())      # Capitalize each word: Python Programming
print(s.replace("python", "java"))  # Replace substring: java Programming
print(s.split())      # Split string into list: ['python', 'Programming']

# -------------------------------
# 8️⃣ F-Strings (Python 3.6+)
# -------------------------------
# Used for easy and readable string formatting
name = "Vinay"
age = 25

# Old way
print("My name is " + name + " and I am " + str(age) + " years old.")

# Using f-string
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Vinay and I am 25 years old.

# -------------------------------
# ✅ Summary for Teaching
# -------------------------------
# 1. Variables store different types of data and are dynamically typed.
# 2. Strings are sequences of characters and can be manipulated using operators and methods.
# 3. F-strings provide a clean way to include variables inside strings.
# 4. String indexing and slicing allow you to access individual characters or parts of strings.
