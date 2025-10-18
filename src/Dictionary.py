# ===============================================
# DICTIONARY METHODS IN PYTHON
# ===============================================

# Create a sample dictionary
person = {
    "name": "Vinay",
    "age": 25,
    "city": "Delhi"
}

# -----------------------------------------------
# 1️⃣ get()
# -----------------------------------------------
# Returns the value for the given key. If key doesn't exist, returns None (or default)
print(person.get("name"))       # Vinay
print(person.get("salary"))     # None
print(person.get("salary", 0))  # 0 (default value)

# -----------------------------------------------
# 2️⃣ keys()
# -----------------------------------------------
# Returns all the keys in the dictionary
print(person.keys())  # dict_keys(['name', 'age', 'city'])

# -----------------------------------------------
# 3️⃣ values()
# -----------------------------------------------
# Returns all the values in the dictionary
print(person.values())  # dict_values(['Vinay', 25, 'Delhi'])

# -----------------------------------------------
# 4️⃣ items()
# -----------------------------------------------
# Returns key-value pairs as tuples
print(person.items())
# dict_items([('name', 'Vinay'), ('age', 25), ('city', 'Delhi')])

# -----------------------------------------------
# 5️⃣ pop()
# -----------------------------------------------
# Removes the key and returns its value
age_value = person.pop("age")
print(age_value)   # 25
print(person)      # {'name': 'Vinay', 'city': 'Delhi'}

# -----------------------------------------------
# 6️⃣ popitem()
# -----------------------------------------------
# Removes the **last inserted** key-value pair and returns it as a tuple
last_item = person.popitem()
print(last_item)   # ('city', 'Delhi')
print(person)      # {'name': 'Vinay'}

# -----------------------------------------------
# 7️⃣ update()
# -----------------------------------------------
# Updates the dictionary with new key-value pairs or modifies existing keys
person.update({"city": "Mumbai", "age": 26})
print(person)  # {'name': 'Vinay', 'city': 'Mumbai', 'age': 26}

# -----------------------------------------------
# 8️⃣ clear()
# -----------------------------------------------
# Removes all items from the dictionary
person.clear()
print(person)  # {}


# ===============================================
# MAP IN JAVA VS DICTIONARY IN PYTHON
# ===============================================

# In Java, we use Map to store key-value pairs.
# In Python, we use Dictionary (dict) for the same purpose.

# -----------------------------------------------
# 1️⃣ Key Features
# -----------------------------------------------
# - Both store key-value pairs
# - Keys must be unique
# - Values can be of any type
# - Both are mutable (can add, remove, or update elements)

# -----------------------------------------------
# 2️⃣ Creating a Dictionary in Python
# -----------------------------------------------
# Using curly braces
person = {"name": "Vinay", "age": 25, "city": "Delhi"}

# Using dict() constructor
person2 = dict(name="Mishra", age=28, city="Mumbai")

# Empty dictionary
empty_dict = {}

# -----------------------------------------------
# 3️⃣ Accessing Values
# -----------------------------------------------
print(person["name"])       # Vinay
print(person.get("age"))    # 25
print(person.get("salary")) # None

# -----------------------------------------------
# 4️⃣ Adding/Updating Items
# -----------------------------------------------
person["salary"] = 50000    # Add new key-value
person["age"] = 26          # Update existing key
print(person)

# -----------------------------------------------
# 5️⃣ Removing Items
# -----------------------------------------------
person.pop("salary")        # Remove key by name
del person["city"]          # Remove using del
print(person)

# -----------------------------------------------
# 6️⃣ Looping Through Dictionary
# -----------------------------------------------
for key, value in person.items():
    print(key, ":", value)

# -----------------------------------------------
# 7️⃣ Comparison Table: Java Map vs Python Dictionary
# -----------------------------------------------
# | Feature                  | Java Map                           | Python Dictionary          |
# |--------------------------|-----------------------------------|----------------------------|
# | Purpose                  | Stores key-value pairs             | Stores key-value pairs     |
# | Key uniqueness           | Keys must be unique                | Keys must be unique        |
# | Value type               | Can be any type (object)           | Can be any type            |
# | Key type                 | Can be any object                  | Must be immutable type     |
# | Mutability               | Mutable (add/remove/update)        | Mutable (add/remove/update)|
# | Common Implementations   | HashMap, TreeMap, LinkedHashMap    | dict                       |
# | Accessing Values         | map.get(key)                       | dict[key] or dict.get(key) |
# | Adding/Updating          | map.put(key, value)                | dict[key] = value          |
# | Removing                 | map.remove(key)                    | dict.pop(key) or del dict[key] |
# | Iteration                | for (Map.Entry<K,V> e : map.entrySet()) | for key, value in dict.items() |
