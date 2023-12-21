#len
my_dict = {"name": "John", "age": 25, "city": "New York"}
length = len(my_dict)
print(length)  # Output: 3

#keys
keys_list = my_dict.keys()
print(keys_list)  # Output: dict_keys(['name', 'age', 'city'])

#values
values_list = my_dict.values()
print(values_list)  # Output: dict_values(['John', 25, 'New York'])

#items
items_list = my_dict.items()
print(items_list)  # Output: dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

#del
del my_dict["age"]
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

#in
print("name" in my_dict)  # Output: True
print("gender" in my_dict)  # Output: False

#get
age = my_dict.get("age", None)
print(age)  # Output: None (default value since "age" is not present)

#setdefault 多一個chartreuse鍵
occupation = my_dict.setdefault("occupation", "Unknown")
print(occupation)  # Output: Unknown (default value since "occupation" is not present)

#copy
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'name': 'John', 'city': 'New York'}

#update
new_data = {"age": 30, "gender": "Male"}
my_dict.update(new_data)
print(my_dict)  # Output: {'name': 'John', 'city': 'New York', 'age': 30, 'gender': 'Male'}
