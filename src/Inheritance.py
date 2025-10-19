# ============================================================
# 🌳 INHERITANCE IN PYTHON
# ============================================================

# 🔹 Inheritance allows a class (child) to acquire attributes and methods of another class (parent)
# 🔹 Helps in code reuse, organization, and implementing polymorphism

# ============================================================
# 1️⃣ Single Inheritance
# ============================================================

# Child class inherits from one parent class

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def showBrand(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def showModel(self):
        print(f"Car Model: {self.model}")

c = Car("Toyota", "Corolla")
c.showBrand()  # From Vehicle
c.showModel()  # From Car


# ============================================================
# 2️⃣ Multiple Inheritance
# ============================================================

# Child class inherits from multiple parent classes

class Engine:
    def start(self):
        print("Engine started")

class Body:
    def color(self):
        print("Color: Red")

class SportsCar(Engine, Body):
    def features(self):
        print("Sports features activated")

s = SportsCar()
s.start()       # From Engine
s.color()       # From Body
s.features()    # From SportsCar


# ============================================================
# 3️⃣ Multilevel Inheritance
# ============================================================

# Chain of inheritance

class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()   # From Animal
d.walk()  # From Mammal
d.bark()  # From Dog


# ============================================================
# 4️⃣ Hierarchical Inheritance
# ============================================================

# Multiple child classes inherit from a single parent

class Shape:
    def area(self):
        print("Calculating area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area")

class Circle(Shape):
    def area(self):
        print("Circle area")

r = Rectangle()
c = Circle()
r.area()  # Rectangle area
c.area()  # Circle area


# ============================================================
# 5️⃣ Hybrid Inheritance
# ============================================================

# Combination of multiple types of inheritance

class A:
    def a_method(self):
        print("A method")

class B(A):
    def b_method(self):
        print("B method")

class C(A):
    def c_method(self):
        print("C method")

class D(B, C):
    def d_method(self):
        print("D method")

d = D()
d.a_method()  # From A
d.b_method()  # From B
d.c_method()  # From C
d.d_method()  # From D


# ============================================================
# 🔹 Key Points About Python Inheritance
# ============================================================

# 1. Python supports multiple inheritance, unlike Java (Java allows only single inheritance for classes, multiple via interfaces)
# 2. Python uses Method Resolution Order (MRO) to determine which parent method to call in multiple inheritance
# 3. super() can be used to call parent constructor/method
# 4. Private attributes (__var) in parent are name-mangled; child cannot access directly

# Example MRO:
print(D.mro())  # Shows method resolution order for class D


# ============================================================
# 🧩 METHOD RESOLUTION ORDER (MRO) IN PYTHON
# ============================================================

# 🔹 Purpose:
# When a class inherits from multiple parents, Python needs to decide
# which parent’s method to call if multiple parents have the same method name.
# MRO defines this lookup order.

# ============================================================
# Example:

class A:
    def show(self):
        print("A show method")

class B(A):
    def show(self):
        print("B show method")

class C(A):
    def show(self):
        print("C show method")

class D(B, C):
    pass

d = D()
d.show()          # ✅ Output: B show method
print(D.mro())    # Shows method resolution order

# Output:
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# 🔹 Explanation:
# Python searches for the method in the following order:
# 1. Current class (D) → Not found
# 2. First parent (B) → Found → B.show() is called
# 3. Next parent (C) → Not checked because method found in B
# 4. A → Not checked
# 5. object → Not checked

# 🔹 Changing parent order affects MRO:

class D2(C, B):
    pass

d2 = D2()
d2.show()         # ✅ Output: C show method
print(D2.mro())

# 🔹 Key Points:
# - MRO ensures consistent method lookup in multiple inheritance
# - Python uses C3 Linearization algorithm for MRO
# - Check MRO using ClassName.mro() or help(ClassName)
# - Important in hybrid or multiple inheritance scenarios
