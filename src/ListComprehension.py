# ============================================================
# 🧩 TOPIC: LIST COMPREHENSION IN PYTHON
# ============================================================

"""
============================================================
📘 INTRODUCTION
------------------------------------------------------------
List comprehension provides a **concise and powerful** way to
create new lists by applying an expression to each item in an
existing iterable (like a list, tuple, or range).

✅ It replaces the need for multi-line loops with a single line.
✅ It can also include optional conditional logic (if/else).
============================================================
"""

# ============================================================
# 🧠 SYNTAX
# ============================================================
"""
[ <expression> for <item> in <iterable> if <condition> ]

🔹 <expression> : Operation or value to include in the new list
🔹 <item>       : Current element from the iterable
🔹 <iterable>   : Sequence like a list, tuple, or range
🔹 <condition>  : (Optional) Filter to include only items that 
                  satisfy the condition
"""

# ============================================================
# ⚙️ EXAMPLE 1: Basic List Comprehension (Square each element)
# ============================================================
a = [2, 3, 4, 5]

# Using list comprehension
res = [val ** 2 for val in a]   # '**' = exponentiation operator
print(res)                      # Output: [4, 9, 16, 25]

"""
🧾 Explanation:
val * 2   → Multiply val by 2
val ** 2  → Square val (val to the power of 2)
val ** 3  → Cube val (val to the power of 3)
"""

# ============================================================
# 🔁 EXAMPLE 2: For Loop vs. List Comprehension
# ============================================================

# --- Traditional For Loop ---
a = [2, 3, 4, 5, 6]
res = []
for val in a:
    res.append(val ** 2)
print(res)    # Output: [4, 9, 16, 25, 36]

"""
🧠 Explanation:
res = []           → Creates an empty list to store results
for val in a:      → Loops through each number in list 'a'
res.append(val**2) → Squares the current number and adds to 'res'
"""

# --- Using List Comprehension ---
a = [2, 3]
res = [ele ** 2 for ele in a]
print(res)    # Output: [4, 9]


# ============================================================
# ⚖️ EXAMPLE 3: Conditional Statement in List Comprehension
# ============================================================
a = [2, 3, 4, 5, 6]
res = [val for val in a if val % 2 == 0]
print(res)    # Output: [2, 4, 6]

"""
🧠 Explanation:
Only even numbers (val % 2 == 0) are added to the new list.

Equivalent to:
res = []
for val in a:
    if val % 2 == 0:
        res.append(val)
"""

# ============================================================
# 🔢 EXAMPLE 4: Creating a List from a Range
# ============================================================
print([i for i in range(10)])   # Output: [0,1,2,3,4,5,6,7,8,9]


# ============================================================
# 🔄 EXAMPLE 5: Nested Loops inside List Comprehension
# ============================================================
print([(i, j) for i in range(3) for j in range(3)])
# Output: [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

"""
🧠 Equivalent Normal Loops:
for i in range(3):
    for j in range(3):
        print((i, j))
"""

# ============================================================
# 🧾 EXAMPLE 6: Flattening a 2D List (Matrix)
# ============================================================
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

res = [val for row in mat for val in row]
print(res)   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
🧠 Step-by-Step:
Equivalent to nested loops:
for row in mat:
    for val in row:
        res.append(val)

1️⃣ Takes row = [1,2,3] → extracts 1,2,3
2️⃣ Takes row = [4,5,6] → extracts 4,5,6
3️⃣ Takes row = [7,8,9] → extracts 7,8,9

Final Result → [1,2,3,4,5,6,7,8,9]
"""

# ============================================================
# 💡 SUMMARY TABLE
# ============================================================
"""
| Use Case                         | Syntax Example                                  | Description                                  |
|----------------------------------|--------------------------------------------------|----------------------------------------------|
| Basic transformation             | [x**2 for x in a]                               | Square each element                          |
| With condition                   | [x for x in a if x%2==0]                        | Filter even numbers                          |
| With if–else                     | [x**2 if x%2==0 else x for x in a]              | Apply logic conditionally                    |
| From range                       | [i for i in range(10)]                          | Generate a sequence of numbers               |
| Nested loop                      | [(i,j) for i in range(3) for j in range(3)]     | Create combinations or pairs                 |
| Flatten a matrix (2D → 1D)       | [val for row in mat for val in row]             | Combine inner lists into one list            |
"""

# ============================================================
# ⚖️ PYTHON vs JAVA COMPARISON
# ============================================================
"""
| Feature                      | Python (List Comprehension)                      | Java (Equivalent Approach)                                   |
|-------------------------------|--------------------------------------------------|--------------------------------------------------------------|
| Syntax simplicity             | Compact: [x*x for x in list if x>0]              | Verbose: for loops or Streams API required                   |
| Readability                   | Short and expressive                             | Longer, more boilerplate                                     |
| Loop nesting                  | Nested directly inside comprehension             | Must use nested for-loops                                    |
| Functional style              | Built-in via comprehension                       | Added in Java 8 with Stream API                              |
| Filtering                     | Using 'if' inside comprehension                  | Using 'filter()' in Streams                                  |
| Transformation                | Apply directly in expression                     | Using 'map()' in Streams                                     |
| Example (filter even numbers) | [x for x in list if x%2==0]                      | list.stream().filter(x->x%2==0).collect(Collectors.toList())  |

✅ **Conclusion:**
- Python’s list comprehension offers **cleaner syntax** and **faster prototyping**.
- Java requires the **Stream API** or multiple lines of code for the same result.
- Both achieve the same functionality, but Python emphasizes **readability**.
"""

# ============================================================
# ✅ CONCLUSION
# ============================================================
"""
✔ List comprehension is one of Python’s most elegant features.
✔ It combines looping, filtering, and expression evaluation in one line.
✔ It is both readable and efficient compared to traditional loops.

💡 Think of it as Python’s version of Java’s Stream API — but simpler!
"""
