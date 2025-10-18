# ============================================================
# 🧠 FUNCTIONS IN PYTHON
# ============================================================

# A function is a block of reusable code that performs a specific task.
# Functions help in organizing code, reducing repetition, and improving readability.

# ----------------------------
# 1️⃣ Defining a Function
# ----------------------------
# In Python, all functions are defined using the 'def' keyword
# Syntax:
# def function_name(parameters):
#     """Optional docstring"""
#     # function body
#     return value

# Example 1: Function without parameters
def greet():
    print("Hello, World!")

greet()

# Example 2: Function with parameters
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# Example 3: Function with default parameters
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

greet_person("Vinay")
greet_person()  # Uses default value

# Example 4: Function with variable number of arguments (*args, **kwargs)
def show_details(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_details(1, 2, 3, name="Vinay", age=25)

# ============================================================
# 🔹 Key Points about Functions
# ============================================================
# - Use 'def' keyword to define functions.
# - Functions can have parameters with default values.
# - *args allows passing variable number of positional arguments.
# - **kwargs allows passing variable number of keyword arguments.
# - Functions can return values using 'return'.
# - Python supports nested functions and anonymous functions (lambda).

# ============================================================
# 2️⃣ Lambda (Anonymous) Functions
# ============================================================
# Lambda functions are small anonymous functions defined using 'lambda' keyword.
# Syntax:
# lambda arguments: expression

square = lambda x: x**2
print("Square:", square(5))

# Lambda with multiple arguments
add_two = lambda a, b: a + b
print("Add:", add_two(10, 15))

# ============================================================
# 3️⃣ Comparison with Java
# ============================================================
# Java functions (methods) vs Python functions

# Feature               | Java                             | Python
# --------------------- | -------------------------------- | ----------------------------
# Keyword for function  | returnType methodName() { ... } | def function_name(): ...
# Return type           | Must specify (int, String, etc) | Optional (dynamic typing)
# Parameters            | Fixed type required              | Dynamic typing (any type)
# Default parameters    | Available (Java 8+)              | Yes, directly in definition
# Anonymous function    | Lambda / Functional interfaces   | lambda keyword
# Variable arguments    | varargs (...)                    | *args, **kwargs

# ============================================================
# ✅ Key Takeaways
# ============================================================
# 1. Functions in Python are defined using 'def'.
# 2. Python functions are dynamically typed; no need to declare return type.
# 3. Default parameters, *args, and **kwargs make functions flexible.
# 4. Lambda functions allow small, anonymous functions.
# 5. Functions improve code reusability and readability.
