# ===============================================
# EXCEPTIONS IN PYTHON
# ===============================================

# -----------------------------------------------
# 1️⃣ What is an Exception?
# -----------------------------------------------
# An exception is an **error that occurs during the execution of a program**.
# When an exception occurs, normal flow of the program is interrupted.
# Python provides mechanisms to handle exceptions so the program can continue running.

# -----------------------------------------------
# 2️⃣ Common Built-in Exceptions
# -----------------------------------------------
# - ZeroDivisionError → division by zero
# - ValueError → invalid value type
# - TypeError → operation on incompatible types
# - IndexError → accessing invalid index in a list/tuple
# - KeyError → accessing a non-existent key in dictionary
# - FileNotFoundError → file operations on non-existent file

# -----------------------------------------------
# 3️⃣ Built-in vs Custom Exceptions
# -----------------------------------------------
# Built-in exceptions are already provided by Python, e.g., ZeroDivisionError, ValueError
# Custom exceptions are created by the user by inheriting from Exception

# Custom Exception Example
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("This is a custom error")
except MyCustomError as e:
    print(e)

# -----------------------------------------------
# 4️⃣ Try and Except
# -----------------------------------------------
# Basic exception handling
try:
    x = 10 / 0   # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")

# -----------------------------------------------
# 5️⃣ Multiple Except Blocks
# -----------------------------------------------
try:
    num = int("abc")  # Raises ValueError
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid conversion to integer")

# -----------------------------------------------
# 6️⃣ Catching Multiple Exceptions in Single Except
# -----------------------------------------------
# Similar to Java's multi-catch (catching multiple exceptions in one block)
try:
    x = int("abc") / 0
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)

# Equivalent Java:
# try {
#     int x = Integer.parseInt("abc") / 0;
# } catch (NumberFormatException | ArithmeticException e) {
#     System.out.println("An error occurred: " + e.getMessage());
# }

# -----------------------------------------------
# 7️⃣ Catch All Exceptions
# -----------------------------------------------
try:
    print(10 / 0)
except Exception as e:
    print("Error occurred:", e)

# -----------------------------------------------
# 8️⃣ Else Block
# -----------------------------------------------
# Executes if no exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is", result)

# -----------------------------------------------
# 9️⃣ Finally Block
# -----------------------------------------------
# Executes **always**, whether exception occurs or not
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("This block always executes")

# -----------------------------------------------
# 🔟 Raising Exceptions
# -----------------------------------------------
# You can raise exceptions manually using `raise`
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

# -----------------------------------------------
# 1️⃣1️⃣ sys.exc_info() for Exception Details
# -----------------------------------------------
# Provides detailed info about the current exception
import sys

try:
    x = 1 / 0
except:
    print("Exception type:", sys.exc_info()[0])   # Like Java e.getClass()
    print("Exception message:", sys.exc_info()[1]) # Like Java e.getMessage()
    print("Traceback object:", sys.exc_info()[2])  # Like Java e.printStackTrace()

# -----------------------------------------------
# 1️⃣2️⃣ Python vs Java Exception Comparison
# -----------------------------------------------
# 1. Python exceptions are **not checked**; Java has checked and unchecked exceptions.
# 2. Python supports try-except-else-finally; Java supports try-catch-finally (no else).
# 3. sys.exc_info() in Python gives type, message, traceback; Java uses e.getClass(), e.getMessage(), e.printStackTrace().
# 4. Python allows raising custom exceptions using `raise`; Java uses `throw`.
# 5. Python supports catching **multiple exceptions in a single except block**; Java supports multi-catch using `|`.
# 6. In Python, exception blocks are defined by **indentation and colon (:);** Java uses braces { }.

# -----------------------------------------------
# 1️⃣3️⃣ Tips for Using Exceptions
# -----------------------------------------------
# 1. Use try-except for operations that may fail (file I/O, division, conversion).
# 2. Avoid catching general Exception unless necessary; prefer specific exceptions.
# 3. Use finally to release resources (files, connections).
# 4. Raise custom exceptions for better error handling.
# 5. Use sys.exc_info() for logging or debugging full exception details.
# 6. Use multiple exceptions in one except block if handling is the same for all.
