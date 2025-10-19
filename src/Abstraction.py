# ============================================================
# 🕵️‍♂️ ABSTRACTION IN PYTHON
# ============================================================

# 🔹 Abstraction is the concept of hiding implementation details
#   and showing only the essential features to the user.

# - Defines what a class should do, not how it does it
# - In Python, abstraction is implemented using the `abc` module

from abc import ABC, abstractmethod

# ============================================================
# 1️⃣ Abstract Class and Abstract Method

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def move(self):   # Abstract method
        pass         # 'pass' = placeholder, no implementation

    @abstractmethod
    def fuel(self):
        pass

# ❌ Cannot create instance of abstract class:
# v = Vehicle()  # Error: Can't instantiate abstract class Vehicle with abstract methods

# ============================================================
# 2️⃣ Subclass Implementing Abstract Methods

class Car(Vehicle):
    def move(self):        # Must implement all abstract methods
        print("Car drives")

    def fuel(self):
        print("Car uses petrol")

c = Car()   # ✅ Works, all abstract methods implemented
c.move()    # Car drives
c.fuel()    # Car uses petrol

# ============================================================
# 3️⃣ Key Points About Abstraction in Python

# 1. Abstract class = inherits from ABC + has at least one @abstractmethod
# 2. Abstract method = defines interface, uses 'pass' as placeholder
# 3. Cannot instantiate abstract class directly
# 4. Subclass must implement all abstract methods to be instantiable
# 5. Partial abstraction allowed (some methods abstract, some concrete)
# 6. Helps hide internal implementation details and define a clear interface

# ============================================================
# ⚔️ Abstraction: Python vs Java

#| Feature                        | Python                          | Java                                 |
#|--------------------------------|---------------------------------|-------------------------------------|
#| Abstract Class                  | Supported (`abc.ABC`)           | Supported (`abstract class`)        |
#| Abstract Method                 | Supported (`@abstractmethod`)   | Supported (`abstract method`)       |
#| Instantiation                   | ❌ Cannot instantiate           | ❌ Cannot instantiate               |
#| Partial Abstraction             | Supported                       | Supported                           |
#| Interfaces                      | Optional (duck typing often enough) | Supported & commonly used        |
#| Placeholder for method body     | `pass`                           | {} or empty method body             |

# ✅ Summary:
# - Abstraction = hide implementation, show only essential features
# - Use ABC + @abstractmethod in Python
# - Use 'pass' as placeholder in abstract methods
# - Subclass must implement all abstract methods to instantiate
