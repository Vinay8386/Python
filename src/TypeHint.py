# ============================================================
# 🧠 TYPE HINTS IN PYTHON
# ============================================================

# ✅ Type hints are a way to tell what type of value a variable,
# function parameter, or return value should have.
# They do NOT enforce type checking at runtime.
# Instead, they help developers, IDEs (like PyCharm/VS Code),
# and static analysis tools (like mypy) detect type mismatches early.

# ------------------------------------------------------------
# 🧩 BASIC TYPE HINTS (No Import Needed)
# ------------------------------------------------------------
# Python supports basic built-in types without any import.

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

message = greet("Vinay", 25)
print(message)   # Output: Hello Vinay, you are 25 years old.


# ------------------------------------------------------------
# 🧩 ADVANCED TYPE HINTS (Need 'typing' Module)
# ------------------------------------------------------------
# For generic or advanced types, import from the typing module.

from typing import List, Dict, Optional, Union

# Example 1: List and Dict type hints (like Java Generics)
def process_scores(scores: List[int]) -> Dict[str, int]:
    return {"max": max(scores), "min": min(scores)}

result = process_scores([45, 67, 89])
print(result)   # Output: {'max': 89, 'min': 45}


# Example 2: Optional Type (Nullable value, like Java Optional)
def find_user(id: int) -> Optional[str]:
    if id == 1:
        return "Vinay"
    return None

print(find_user(1))   # Output: Vinay
print(find_user(2))   # Output: None


# Example 3: Union Type (Multiple allowed types)
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

print(add(10, 5.5))   # Output: 15.5


# Python 3.10+ allows shorter syntax using '|'
def add_v2(a: int | float, b: int | float) -> int | float:
    return a + b


# ------------------------------------------------------------
# 🧩 RUNTIME VS STATIC BEHAVIOR
# ------------------------------------------------------------
# ✅ Type hints DO NOT restrict values at runtime:
def show_type(value: int):
    print(value)

show_type("Hello")    # ✅ Works fine, though logically wrong
# (It will NOT throw an error — type hints are ignored at runtime)


# ------------------------------------------------------------
# 🧩 STATIC TYPE CHECKING USING 'mypy'
# ------------------------------------------------------------
# mypy can check type correctness before runtime (like Java compiler).
# Command:
#   pip install mypy
#   mypy your_file.py
#
# Example output (if type mismatch found):
#   error: Argument 1 to "show_type" has incompatible type "str"; expected "int"


# ------------------------------------------------------------
# 🧩 IDE SUPPORT
# ------------------------------------------------------------
# - PyCharm, VS Code, and most modern IDEs natively understand type hints.
# - They suggest autocompletion, detect mismatched types,
#   and improve readability — no plugin required.

# ------------------------------------------------------------
# ✅ SUMMARY TABLE
# ------------------------------------------------------------

# | Purpose                    | Import Needed? | Example / Notes                        |
# |-----------------------------|----------------|----------------------------------------|
# | Basic built-in types        | ❌ No           | str, int, float, bool, list, dict      |
# | Generic / Advanced types    | ✅ Yes          | from typing import List, Dict, Union   |
# | Runtime type checking       | ❌ No           | Type hints ignored at runtime          |
# | Compile-time checking       | Optional        | mypy for static type analysis          |
# | IDE Support                 | ✅ Built-in     | PyCharm, VS Code, etc.                 |

# ============================================================
# 💡 CONCLUSION
# ------------------------------------------------------------
# Type hints make Python code more readable, maintainable,
# and closer to statically typed languages like Java.
# They help catch type-related bugs early and improve code clarity.
# ============================================================


