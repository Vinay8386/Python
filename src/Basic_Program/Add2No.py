# ============================================================
# 📘 PROGRAM: Add Two Numbers in Python
# ============================================================

"""
============================================================
📌 INTRODUCTION
------------------------------------------------------------
This program demonstrates **different ways to add two numbers** in Python:

1. Using the '+' operator
2. Using a class with `__str__()` (similar to Java's toString())
3. Taking user input
4. Using a lambda function
5. Using `operator.add`
6. Using `sum()`
============================================================
"""

# ============================================================
# 🧮 1️⃣ SIMPLE ADDITION USING '+' OPERATOR
# ============================================================
a = 2
b = 3
result = a + b
print(result)   # Output: 5

"""
🧠 Explanation:
- The simplest way to add numbers in Python is using the '+' operator.
- Direct addition returns the sum.
"""

# ============================================================
# 🧩 2️⃣ CLASS-BASED APPROACH TO ADD TWO NUMBERS
# ============================================================
class Add2No:
    """
    ============================================================
    💡 CLASS: Add2No
    ------------------------------------------------------------
    Description:
        Demonstrates how to perform addition using a class in Python.

    Equivalent to:
        Java program where we create a class with two variables,
        define a method to add them, and override the 'toString()'
        method to print the object directly.

    Constructor:
        __init__(self, a, b)
            Initializes the object with two instance variables 'a' and 'b'.

    Methods:
        add(self)
            Returns the sum of 'a' and 'b'.

        __str__(self)
            Overrides the default string representation method so that
            printing the object directly shows the sum instead of the
            memory address (similar to overriding toString() in Java).
    ============================================================
    """

    def __init__(self, a, b):
        """
        ------------------------------------------------------------
        🏗️ Constructor: Initializes the values of a and b
        ------------------------------------------------------------
        Parameters:
            a (int): First number
            b (int): Second number
        """
        self.a = a
        self.b = b

    def add(self):
        """
        ------------------------------------------------------------
        ➕ Method: add
        ------------------------------------------------------------
        Description:
            Returns the sum of 'a' and 'b'.

        Returns:
            int: The result of addition (a + b)
        """
        return self.a + self.b

    def __str__(self):
        """
        ------------------------------------------------------------
        🧾 Method: __str__
        ------------------------------------------------------------
        Description:
            Overrides the default string representation of the object.

        Notes:
            - If not overridden, Python prints something like:
              <__main__.ClassName object at memory_location>
            - In Java, the default output looks like:
              ClassName@HashCode
            - 'toString()' in Java and '__str__()' in Python
              serve the same purpose: returning a human-readable
              string representation of an object.

        Returns:
            str: A formatted message showing the sum of a and b
        ------------------------------------------------------------
        """
        return f"The sum of {self.a} and {self.b} is {self.add()}"

# ============================================================
# 🚀 OBJECT CREATION AND METHOD CALL
# ============================================================
res = Add2No(5, 7)

# Printing the object directly automatically calls __str__()
print(res)    # Output: The sum of 5 and 7 is 12

# ============================================================
# 🧩 3️⃣ ADD TWO NUMBERS USING USER INPUT
# ============================================================
a = input("First number: ")
b = input("Second number: ")

# Convert input to float and add
result = float(a) + float(b)
print(int(result))

# ============================================================
# 🧩 4️⃣ ADD TWO NUMBERS USING LAMBDA FUNCTION
# ============================================================
res = lambda a, b: a + b
print(res(10, 5))  # Output: 15

"""
🧠 Explanation:
- `lambda a, b: a + b` creates an anonymous function to add two numbers.
- Must call the lambda with values (e.g., res(10, 5)) to get the sum.
"""

# ============================================================
# 🧩 5️⃣ ADD TWO NUMBERS USING operator.add
# ============================================================
import operator
print(operator.add(10, 5))  # Output: 15

"""
🧠 Explanation:
- Python's `operator` module provides built-in functions for arithmetic.
- `operator.add(a, b)` is equivalent to `a + b`.
"""

# ============================================================
# 🧩 6️⃣ ADD TWO NUMBERS USING sum()
# ============================================================
print(sum([10, 5]))  # Output: 15

"""
🧠 Explanation:
- `sum()` can add multiple numbers in a list or iterable.
- Useful when adding more than two numbers.
"""

# ============================================================
# ✅ SUMMARY
# ============================================================
"""
✔ Python provides multiple ways to add numbers: using '+', classes, lambda functions, operator module, and sum().
✔ Class-based approach allows overriding `__str__()` to display human-readable results (like Java's toString()).
✔ Lambda functions provide a concise way to perform addition without defining a full function.
✔ The operator module and sum() are helpful for more functional programming or when dealing with iterables.
"""
