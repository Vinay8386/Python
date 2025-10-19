# ============================================================
# 📂 WORKING WITH FILES IN PYTHON
# ============================================================

# 🔹 Python provides built-in functions to **read, write, and manipulate files**.
# 🔹 Common file modes:
#   - 'r'  → Read (default)
#   - 'w'  → Write (creates new file or truncates existing)
#   - 'a'  → Append (adds content to the end)
#   - 'x'  → Create (fails if file exists)
#   - 'b'  → Binary mode (e.g., 'rb', 'wb')
#   - '+'  → Read and write (e.g., 'r+', 'w+')

# ============================================================
# 1️⃣ Opening and Closing Files

# Using open() and close()
f = open("example.txt", "w")  # Open file in write mode
f.write("Hello Python Files!\n")
f.write("This is a second line.\n")
f.close()  # Always close the file to save changes

# ============================================================
# 2️⃣ Reading Files

# Open file in read mode
f = open("example.txt", "r")
content = f.read()  # Read entire file
print(content)
f.close()

# Read line by line
f = open("example.txt", "r")
for line in f:
    print(line.strip())  # strip() removes newline characters
f.close()

# ============================================================
# 3️⃣ Using 'with' Statement (Recommended)

# Automatically closes file after block
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Writing with 'with'
with open("example.txt", "a") as f:
    f.write("Appended line using 'with'.\n")

# ============================================================
# 4️⃣ Working with Binary Files

# Writing binary data
with open("example.bin", "wb") as f:
    f.write(b'\x00\xFF\x10\x20')  # Binary bytes

# Reading binary data
with open("example.bin", "rb") as f:
    data = f.read()
    print(data)  # b'\x00\xFF\x10\x20'

# ============================================================
# 5️⃣ File Methods

# f.read(size)       → Read specified number of bytes
# f.readline()       → Read a single line
# f.readlines()      → Read all lines into a list
# f.write(string)    → Write string to file
# f.writelines(list) → Write list of strings to file

# ============================================================
# 6️⃣ Key Points

# 1. Always close files or use 'with' to prevent data loss
# 2. File modes determine operations allowed
# 3. Binary mode required for non-text files (images, audio)
# 4. Use exception handling to catch errors while working with files

# Example with exception handling:

try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error reading file!")

# ============================================================
# ✅ Summary:

# - Python makes file handling simple with open(), read(), write(), and 'with'
# - Use correct file mode for your operation
# - Always handle exceptions for safer file operations
