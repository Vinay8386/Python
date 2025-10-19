# ============================================================
# 🧠 LIST AND TYPE SAFETY IN PYTHON
# ============================================================

# ✅ 1. BASIC UNDERSTANDING
# ------------------------------------------------------------
# In Python, a list is a built-in data structure that can hold
# multiple elements. Unlike Java’s ArrayList or arrays, Python lists
# are *heterogeneous* — meaning they can store mixed data types.

list_ex = [1, 2, 3, "Vinay", True]
print(list_ex)
# Output: [1, 2, 3, 'Vinay', True]

# This runs perfectly because Python is *dynamically typed*.
# That means it checks types at runtime, not at compile time.


# ⚠️ 2. POTENTIAL ISSUE WITH MIXED TYPES
# ------------------------------------------------------------
# The flexibility of storing different data types can lead to
# runtime errors or incorrect results if data types get mixed up
# unintentionally.

numbers = [1, 2, "3", 4]   # "3" is a string instead of an integer
total = 0
for n in numbers:
    total += n             # ❌ Will fail at runtime

# Output:
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# Python does not stop you at the declaration stage — it fails only
# when the operation involves incompatible types.


# 🧩 3. WAYS TO PREVENT SUCH MISTAKES
# ------------------------------------------------------------

# ✅ Option 1: Type Hints (Recommended for clarity)
# Type hints don’t enforce types at runtime but help tools like
# mypy, PyCharm, or VS Code detect type mismatches early.

from typing import List

def calculate_sum(numbers: List[int]) -> int:
    total = 0
    for n in numbers:
        total += n
    return total

# mypy or IDE will warn you if you call:
# calculate_sum([1, 2, "3"])  # ❌ Incorrect type


# ✅ Option 2: Runtime Type Checking (Strict validation)
# You can manually check the data type at runtime.

def calculate_sum_safe(numbers):
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError(f"Invalid element {n} of type {type(n)}")
    return sum(numbers)

print(calculate_sum_safe([1, 2, 3]))      # ✅ Works fine
# print(calculate_sum_safe([1, "2", 3]))  # ❌ Raises TypeError


# ✅ Option 3: Data Validation Libraries (Used in large projects)
# For real-world applications, especially in APIs or ML pipelines,
# developers use validation libraries like:
# - pydantic (used in FastAPI)
# - marshmallow
# - dataclasses (for structured data)
# These enforce type correctness automatically during initialization.


# 🧠 4. PYTHON VS JAVA COMPARISON TABLE
# ------------------------------------------------------------

# | Feature             | Java                            | Python                          |
# |---------------------|----------------------------------|----------------------------------|
# | Type Checking       | Compile-time                     | Runtime                         |
# | List Type           | Homogeneous (List<Integer>)      | Heterogeneous                   |
# | Mistyped Element    | Compile-time Error               | Runtime Error / Logic Bug        |
# | Type Safety Tools   | JVM Enforced                     | Type Hints / Linter Tools        |

# ✅ Real-world Analogy:
# Python list → Like a mixed *bag*, you can put anything inside.
# Java ArrayList<Integer> → Like a *tray labeled “Integers only”*.
# The tray (Java) will stop you if you try to drop a string in it.


# ✅ 5. FINAL CONCLUSION
# ------------------------------------------------------------
# ✔ Python allows mixed data types in a list.
# ✔ But this flexibility requires developer discipline.
# ✔ Use type hints, validation, or runtime checks to maintain data integrity.
# ✔ Always validate or sanitize your list inputs in real-world projects.
