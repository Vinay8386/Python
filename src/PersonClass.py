# ============================================================
# 🧠 CLASSES & CONSTRUCTORS IN PYTHON
# ============================================================

# A class is a blueprint for creating objects.
# It contains attributes (data) and methods (functions) defining the behavior of the object.

# ----------------------------
# 1️⃣ Defining a Class
# ----------------------------
class Person:
    # Class attribute (shared by all instances)
    species = "Human"

    # Constructor (__init__)
    # Called automatically when a new object is created
    # 'self' refers to the current instance (like 'this' in Java)
    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute

    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of Person
p = Person("Vinay", 25)
p.greet()

# ============================================================
# 🔹 Key Points about Classes
# ============================================================
# - 'class' keyword is used to define a class.
# - Class attributes are shared by all objects.
# - Instance attributes are unique to each object.
# - Methods in a class must have 'self' as the first parameter.
# - Python supports inheritance, polymorphism, and encapsulation.

# ============================================================
# 2️⃣ Constructor in Python (__init__)
# ============================================================

# In Python:
# - Constructors are always defined using __init__()
# - They are automatically called when an object is created
# - Unlike Java, constructor name is NOT the class name
# - 'self' refers to the object being created
# - Python supports only one constructor per class (use default arguments for overloading)

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

# Creating objects
e1 = Employee("Alice", 101)
e2 = Employee("Bob", 102)

e1.display()
e2.display()

# ============================================================
# 🔹 Default Constructor
# ============================================================
# If __init__ is not defined, Python provides a default constructor

class Car:
    pass

c = Car()  # Works fine even without defining __init__()

# ============================================================
# 🔹 Constructor Overloading (Using Default Arguments)
# ============================================================

class Person2:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

p1 = Person2("Vinay", 25)  # Uses provided values
p2 = Person2()              # Uses default values

print(p1.name, p1.age)  # Vinay 25
print(p2.name, p2.age)  # None 0

# ============================================================
# 🔹 Calling Parent Constructor (Inheritance)
# ============================================================

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls parent constructor
        print("Child constructor")

c = Child()

# Output:
# Parent constructor
# Child constructor

# ============================================================
# 🔹 Java vs Python Constructor Comparison
# ============================================================

# Feature                   Java                       Python
# ---------------------------------------------------------------
# Constructor Name           Same as class name         __init__()
# Called Automatically       ✅ Yes                     ✅ Yes
# Default Constructor        ✅ Yes                     ✅ Yes
# Constructor Overloading    ✅ Yes                     ❌ No (use default args)
# Parent Constructor         super()                    super().__init__()
# Current Object             this                        self
# Access Modifiers           public/private/protected   Not required

# ============================================================
# ✅ Key Takeaways
# ============================================================

# 1. 'class' defines a blueprint for objects in Python.
# 2. 'self' in Python is equivalent to 'this' in Java.
# 3. Constructors are always __init__(), never use class name.
# 4. Python automatically calls __init__() when object is created.
# 5. Default constructor exists if __init__() is not defined.
# 6. Only one constructor per class; use default arguments for flexibility.
# 7. Use super().__init__() to call parent constructor in inheritance.
