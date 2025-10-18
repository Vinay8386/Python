# ===============================================
# IF-ELSE STATEMENTS IN PYTHON
# ===============================================

# -----------------------------------------------
# 1️⃣ Simple IF Statement
# -----------------------------------------------
# Executes a block of code only if the condition is True

x = 10

if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# -----------------------------------------------
# 2️⃣ IF-ELSE Statement
# -----------------------------------------------
# Executes one block if condition is True, another if False

x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")  # Output: x is not greater than 5

# -----------------------------------------------
# 3️⃣ IF-ELIF-ELSE Statement
# -----------------------------------------------
# Used to check multiple conditions sequentially

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")  # Output: Grade: B
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# ✅ Conditions are checked from top to bottom.
# ✅ First condition that evaluates to True executes, others are skipped.

# -----------------------------------------------
# 4️⃣ Nested IF Statements
# -----------------------------------------------
# An if or if-else inside another if or else

x = 10
y = 20

if x > 5:
    if y > 15:
        print("Both conditions are True")  # Output: Both conditions are True
    else:
        print("x>5 but y<=15")
else:
    print("x<=5")

# -----------------------------------------------
# 5️⃣ Inline IF (Ternary Operator)
# -----------------------------------------------
# Conditional expression in one line
x = 10

result = "Greater than 5" if x > 5 else "5 or less"
print(result)  # Output: Greater than 5

# ✅ Syntax:
# expression_if_true if condition else expression_if_false

# Can also be used in list comprehension
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if x%2==0 else "Odd" for x in numbers]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# -----------------------------------------------
# 6️⃣ Multiple Conditions using AND / OR
# -----------------------------------------------
x = 10
y = 5

if x > 5 and y < 10:
    print("Both conditions are True")  # Output: Both conditions are True

if x > 15 or y < 10:
    print("At least one condition is True")  # Output: At least one condition is True

# -----------------------------------------------
# 7️⃣ Summary Table
# -----------------------------------------------
# | Case | Syntax Example | Description |
# |------|----------------|-------------|
# | Simple if | if condition: | Executes block if True |
# | If-else | if condition: else: | Executes one of two blocks |
# | If-elif-else | if cond1: elif cond2: else: | Multiple conditions |
# | Nested if | if cond1: if cond2: | If inside another if |
# | Inline if | expr1 if cond else expr2 | One-liner conditional expression |
# | Multiple conditions | if cond1 and/or cond2: | Combine conditions with logical operators |

