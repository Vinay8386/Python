# ============================================================
# 🔄 POLYMORPHISM IN PYTHON
# ============================================================

# 🔹 Polymorphism means "many forms".
# - A single function, method, or operator can behave differently depending on the context.
# - It allows **code reusability** and **flexible programming**.

# ============================================================
# 1️⃣ Polymorphism with Functions (Duck Typing)

# In Python, we can pass different types of objects to the same function
# as long as they implement the required behavior.

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()  # Works for any object with 'speak' method

d = Dog()
c = Cat()

make_sound(d)  # Bark
make_sound(c)  # Meow

# 🔹 Explanation:
# - Python does not care about the type of object.
# - If the object has the required method, it works.
# - This is called **duck typing**: "If it walks like a duck and quacks like a duck, it’s a duck."


# ============================================================
# 2️⃣ Polymorphism with Inheritance (Method Overriding)

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Car drives")

class Bike(Vehicle):
    def move(self):
        print("Bike rides")

vehicles = [Car(), Bike(), Vehicle()]

for v in vehicles:
    v.move()  # Calls the correct overridden method based on object type

# Output:
# Car drives
# Bike rides
# Vehicle moves


# ============================================================
# 3️⃣ Polymorphism with Operators (Operator Overloading)

# Python allows the same operator to behave differently based on operand types

print(5 + 10)       # 15 → integers addition
print("Hi " + "You") # Hi You → string concatenation
print([1,2] + [3,4]) # [1,2,3,4] → list concatenation


# ============================================================
# 🔹 Key Points in Python
# ============================================================

# 1. Polymorphism is **implicit** (dynamic typing / duck typing)
# 2. Achieved through:
#    - Function/method overloading (Python supports limited overloading via default args)
#    - Method overriding (inheritance)
#    - Operator overloading
# 3. Python resolves method calls at runtime (dynamic polymorphism)
# 4. No need for explicit interfaces; any object with required methods works


# ============================================================
# ⚔️ Polymorphism: Python vs Java
# ============================================================

# | Feature                        | Python                          | Java                                 |
# |--------------------------------|---------------------------------|-------------------------------------|
# | Type Checking                   | Dynamic (duck typing)           | Static (compile-time type checking) |
# | Method Overriding               | Supported                       | Supported                           |
# | Method Overloading              | Limited (default args, *args)  | Supported                           |
# | Operator Overloading            | Supported                       | Limited (cannot overload operators) |
# | Interfaces                      | Not required (duck typing)      | Required to define behavior across classes |
# | Compile-Time vs Runtime         | Mostly runtime (dynamic)        | Mostly compile-time (static)        |

# ✅ Summary:
# - Python polymorphism is **dynamic**, flexible, and based on behavior rather than explicit type.
# - Java polymorphism is **static**, stricter, requires interfaces or explicit type hierarchy.
# - Python’s duck typing allows writing **more generic and reusable code**.
