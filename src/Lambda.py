# ============================================================
# 🧩 TOPIC: LAMBDA FUNCTIONS IN PYTHON (WITH MAP, FILTER, REDUCE)
# ============================================================

"""
============================================================
📘 INTRODUCTION
------------------------------------------------------------
- In Python, the `def` keyword is used to define **normal functions**.
- The `lambda` keyword is used to define **anonymous functions** (functions without a name).
- Lambda functions are concise and useful for **small operations**.
- Commonly used with **map(), filter(), reduce()** and **list comprehensions**.
============================================================
"""

# ============================================================
# 🧠 SYNTAX OF LAMBDA FUNCTIONS
# ============================================================
"""
lambda arguments: expression

- `arguments` → input parameters
- `expression` → single expression evaluated and returned automatically
- Lambda cannot have multiple statements
"""

# ============================================================
# ⚙️ EXAMPLE 1: BASIC LAMBDA FUNCTION
# ============================================================
s1 = 'Vinay'
s2 = lambda func: func.upper()
print(s1)        # Output: Vinay
print(s2(s1))    # Output: VINAY

# ============================================================
# ⚡ EXAMPLE 2: USING MAP() WITH LAMBDA
# ============================================================
# map(func, iterable) → applies func to each element
numbers = [1, 2, 3, 4, 5]

# Square each number using lambda
squared = list(map(lambda x: x**2, numbers))
print(squared)   # Output: [1, 4, 9, 16, 25]

# ============================================================
# ⚡ EXAMPLE 3: USING FILTER() WITH LAMBDA
# ============================================================
# filter(func, iterable) → keeps elements where func returns True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# ============================================================
# ⚡ EXAMPLE 4: USING REDUCE() WITH LAMBDA
# ============================================================
# reduce(func, iterable) → applies func cumulatively to elements
from functools import reduce

# Sum all numbers
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 15

# Multiply all numbers
product_numbers = reduce(lambda x, y: x * y, numbers)
print(product_numbers)  # Output: 120

# ============================================================
# ⚙️ EXAMPLE 5: LAMBDA WITH CONDITIONAL EXPRESSIONS
# ============================================================
checkNumber = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
print(checkNumber(5))    # Output: positive
print(checkNumber(-5))   # Output: negative
print(checkNumber(0))    # Output: zero

checkEvenOrOdd = lambda x: "even" if x % 2 == 0 else "odd"
print(checkEvenOrOdd(5))  # Output: odd

# ============================================================
# ⚙️ EXAMPLE 6: LAMBDA WITH LIST COMPREHENSION
# ============================================================
funcs = [lambda args=x: args*10 for x in range(1, 5)]
for f in funcs:
    print(f())  # Output: 10, 20, 30, 40

# ============================================================
# ⚡ USING MULTIPLE STATEMENTS
# ============================================================
"""
- Python lambda: only **one expression**, cannot have multiple statements.
- Use normal functions with def if multiple statements are needed.
"""

def double_and_print(x):
    print(x)
    return x * 2

print(double_and_print(5))  # Output: prints 5 and returns 10

# ============================================================
# ⚖️ LAMBDA VS NORMAL FUNCTION
# ============================================================
"""
| Feature                   | Lambda Function                  | Normal Function (def)          |
|---------------------------|---------------------------------|--------------------------------|
| Name                      | Anonymous                        | Named                          |
| Statements Allowed         | Only 1                           | Multiple                       |
| Return                     | Implicit                         | Explicit return required       |
| Syntax                     | lambda args: expression          | def func(args): ...            |
| Use Case                   | Small, temporary functions       | Large, reusable functions     |
| Example                    | lambda x: x*2                    | def double(x): return x*2      |
"""

# ============================================================
# ⚖️ PYTHON LAMBDA vs JAVA LAMBDA COMPARISON
# ============================================================
"""
| Feature                      | Python Lambda                         | Java Lambda / Anonymous Function           |
|-------------------------------|--------------------------------------|-------------------------------------------|
| Syntax simplicity             | lambda x: x*2                         | (x) -> x*2                                |
| Function type                 | Anonymous, single expression          | Anonymous, can be single or multi-statement |
| Return                        | Implicit                               | Explicit required for multi-statement     |
| Conditional logic             | Inline with ternary `a if cond else b` | Use ternary `(cond ? a : b)` or block     |
| Use with collections          | map, filter, reduce, list comp        | Streams API: map(), filter(), reduce()    |
| Capturing variables           | Use default argument `args=x`         | Effectively final variables are captured  |
| Multiple statements           | ❌ Not allowed                         | ✅ Allowed with { }                        |
"""

# ============================================================
# ✅ SUMMARY
# ============================================================
"""
✔ Lambda functions are anonymous, single-expression functions.
✔ Can be used with map(), filter(), reduce(), and list comprehensions.
✔ Conditional expressions can be embedded in lambdas for concise code.
✔ For multiple statements, normal functions (def) must be used.
✔ Python lambdas are limited compared to Java lambdas, which allow multi-statement operations.
"""
