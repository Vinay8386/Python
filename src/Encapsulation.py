# ============================================================
# ⚔️ ENCAPSULATION: PYTHON VS JAVA
# ============================================================

# 🔹 Python Example
# Python uses naming conventions (_var, __var) but does not enforce private variables.

class BankAccountPython:
    def __init__(self, balance):
        self._balance = balance  # Protected by convention

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def getBalance(self):
        return self._balance

acc_py = BankAccountPython(1000)
print(acc_py.getBalance())  # ✅ 1000
acc_py._balance = 5000       # ❌ Direct access still possible
print(acc_py.getBalance())  # 5000

# 🔹 Java Example
# Java enforces private variables, must use getter/setter.

# class BankAccountJava {
#     private int balance;
#
#     public BankAccountJava(int balance) {
#         this.balance = balance;
#     }
#
#     public void deposit(int amount) {
#         if(amount > 0) this.balance += amount;
#     }
#
#     public int getBalance() {
#         return balance;
#     }
# }
# BankAccountJava accJava = new BankAccountJava(1000);
# System.out.println(accJava.getBalance());  // ✅ 1000
# accJava.balance = 5000;                    // ❌ Compilation Error: cannot access private variable

# 🔹 Summary of Differences

# | Feature             | Python                     | Java                       |
# |--------------------|----------------------------|----------------------------|
# | Access control      | By convention (_var)       | Enforced (private)         |
# | Getter/Setter       | Optional, recommended      | Mandatory for private vars |
# | Data hiding         | Weak (can still access)    | Strong (cannot access)     |
# | Validation          | Use methods or @property   | Use getters/setters        |


# ============================================================
# 🏷️ @PROPERTY & @SETTER IN PYTHON
# ============================================================

# 🔹 Purpose:
# - Provide controlled access to attributes (encapsulation)
# - Allow validation when setting values
# - Keep clean, Pythonic syntax (access like a normal attribute)

class BankAccountProperty:
    def __init__(self, balance):
        self._balance = balance  # Internal/protected attribute

    # Getter method using @property
    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    # Setter method using @balance.setter
    @balance.setter
    def balance(self, amount):
        """Setter with validation"""
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount!")

# 🔹 Usage:

acc = BankAccountProperty(1000)

print(acc.balance)    # ✅ Calls getter → 1000
acc.balance = 2000    # ✅ Calls setter → updates value
print(acc.balance)    # 2000
acc.balance = -500    # ❌ Calls setter → prints "Invalid amount!"

# 🔹 Key Points:
# - _balance: internal attribute, protected by convention
# - @property: turns method into a getter property
# - @balance.setter: defines a setter to control assignment
# - acc.balance: calls getter automatically
# - acc.balance = value: calls setter automatically
# - Advantage: Encapsulation + readable, Pythonic code


# ============================================================
# 🔒 ENCAPSULATION IN PYTHON: SOLUTIONS
# ============================================================

# 🔹 Problem:
# Python does not enforce private variables.
# Direct access is possible, which may break data integrity.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected by convention

acc = BankAccount(1000)
print(acc._balance)  # ❌ Direct access is possible, not recommended


# ============================================================
# ⚙️ Solution 1: Using Methods (Getter & Setter)
# ============================================================

class BankAccountMethods:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid amount!")

    def getBalance(self):
        return self._balance

acc1 = BankAccountMethods(1000)
print(acc1.getBalance())  # ✅ 1000
acc1.deposit(500)
print(acc1.getBalance())  # ✅ 1500


# ============================================================
# ⚙️ Solution 2: Using @property (Pythonic Way)
# ============================================================

class BankAccountProperty:
    def __init__(self, balance):
        self._balance = balance

    # @property turns a method into a “getter” for an attribute.
    # It allows you to access a method like an attribute, keeping validation or computation hidden.
    @property
    def balance(self):
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance with validation"""
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount!")

acc2 = BankAccountProperty(1000)
print(acc2.balance)  # Getter ✅ 1000
acc2.balance = 2000  # Setter ✅
print(acc2.balance)  # 2000
acc2.balance = -500  # ❌ Invalid amount!


# ============================================================
# 🏆 Which is Better?
# ============================================================

# 1️⃣ Using Methods:
# - Explicit getter/setter methods
# - Clear to beginners, easy to understand
# - Slightly more verbose

# 2️⃣ Using @property:
# - Cleaner, more Pythonic
# - Looks like direct attribute access
# - Allows validation & control
# - Recommended for modern Python code

# ✅ Conclusion:
# Use @property for better readability, control, and Pythonic style.
# Getter/Setter methods are still valid but more verbose.
