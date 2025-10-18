# ===============================================
# WHILE LOOP IN PYTHON
# ===============================================

# -----------------------------------------------
# 1️⃣ What is a While Loop?
# -----------------------------------------------
# A while loop repeatedly executes a block of code **as long as a condition is True**.

# Syntax:
# while condition:
#     # code block
#     # update variables (to eventually break the loop)

# -----------------------------------------------
# 2️⃣ Simple While Loop Example
# -----------------------------------------------
i = 1
while i <= 5:
    print("Iteration:", i)
    i += 1  # Increment to avoid infinite loop

# -----------------------------------------------
# 3️⃣ While Loop with Else
# -----------------------------------------------
# Python allows an optional else block that executes **only if the loop ends normally** (not by break)
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")  # Executes because loop ended normally

# If loop is terminated by break, else is skipped
i = 1
while i <= 3:
    print(i)
    if i == 2:
        break
    i += 1
else:
    print("Loop finished")  # Will NOT execute

# -----------------------------------------------
# 4️⃣ Infinite While Loop
# -----------------------------------------------
count = 0
while True:
    print("Infinite loop iteration:", count)
    count += 1
    if count >= 3:
        break

# -----------------------------------------------
# 5️⃣ Using Continue in While Loop
# -----------------------------------------------
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# -----------------------------------------------
# 6️⃣ Nested While Loop
# -----------------------------------------------
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# -----------------------------------------------
# 7️⃣ Practical Example: Sum of Numbers
# -----------------------------------------------
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum =", sum)  # Output: Sum = 15

# -----------------------------------------------
# 8️⃣ Python vs Java: While-Else
# -----------------------------------------------
# Python allows `else` with while, Java does NOT.
# Python else executes only if the loop ends naturally (without break)
i = 1
while i <= 2:
    print(i)
    i += 1
else:
    print("Loop finished")  # Executes

# In Java, to mimic else behavior, you must use a flag:
# boolean completed = true;
# while(condition) { ... if(break) { completed=false; break; } }
# if(completed) { ... }

# -----------------------------------------------
# 9️⃣ Features Comparison: Python vs Java While Loop
# -----------------------------------------------
# Features in Python only:
# 1. while-else block (executes if loop ends normally)
# 2. Dynamic typing in condition evaluation (no need for explicit types)
# 3. Can iterate over sequences directly using iterators (with break/continue)
# 4. Infinite loops easily created with `while True`

# Features in Java only:
# 1. Type-safe loop conditions (must be boolean)
# 2. Must explicitly declare and manage variable types
# 3. No direct while-else construct
# 4. Often used with traditional for-loops for indexed iteration

# -----------------------------------------------
#  🔟 Tips for Using While Loop
# -----------------------------------------------
# 1. Always ensure the loop condition will eventually become False or use break.
# 2. Use continue to skip certain iterations.
# 3. Use else to execute a block after normal completion.
# 4. While loops are often used when the number of iterations is unknown or depends on a condition.
