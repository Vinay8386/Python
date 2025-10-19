# ============================================================
# 🧠 OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
# ============================================================

# Everything in Python is an object.
# A class is a blueprint, an object is an instance of a class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)  # Output: Toyota Corolla


# ============================================================
# ⚙️ METHODS IN PYTHON
# ============================================================

# Action-only method (does not return)
class Car:
    def displayInfo(self):
        print(f"Car: {self.brand} {self.model}")

my_car.displayInfo()  # Call directly


# Value-returning method
def getBrand(self):
    return self.brand

print(my_car.getBrand())


# ============================================================
# 🔒 ENCAPSULATION
# ============================================================

# _var → protected by convention
# __var → private (name mangling)

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected by convention

# Using getter and setter
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def getBalance(self):
        return self._balance

acc = BankAccount(1000)
print(acc.getBalance())  # 1000
acc.deposit(2000)
print(acc.getBalance())  # 3000


# ============================================================
# 📝 USING @PROPERTY (PYTHONIC WAY)
# ============================================================

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount")

acc = BankAccount(1000)
print(acc.balance)   # Getter
acc.balance = 5000   # Setter
print(acc.balance)


# ============================================================
# 🖋️ STRING FORMATTING
# ============================================================

# f-string (Python 3.6+)
print(f"Car: {my_car.brand} {my_car.model}")

# Concatenation
print("Car: " + my_car.brand + " " + my_car.model)

# str.format()
print("Car: {} {}".format(my_car.brand, my_car.model))


# ============================================================
# ✅ SUMMARY
# ============================================================

# - OOP in Python: Classes, Objects, Methods, Inheritance, Polymorphism, Abstraction
# - Encapsulation: by convention (_var / __var) or @property for control
# - f-strings are preferred for clean formatting
