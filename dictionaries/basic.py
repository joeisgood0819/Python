# Creating a Dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}

#Accessing Values Using Keys:
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 25

# Adding and Updating Key-Value Pairs:
my_dict["occupation"] = "Engineer"
# Updating an existing value
my_dict["age"] = 26

# Removing Key-Value Pairs:
del my_dict["city"]

#Checking if a Key Exists:
print("name" in my_dict)  # Output: True
print("gender" in my_dict)  # Output: False

# Getting keys and values
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())

# Iterating through keys
for key in my_dict:
    print(key)
# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
