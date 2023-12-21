#`str.format(*args, **kwargs)`:

# Positional Arguments:
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

#Indexed Placeholders:
name = "Bob"
age = 25
message = "My name is {0} and I am {1} years old.".format(name, age)
print(message)

# Named Placeholders:
info = {"name": "Charlie", "age": 35}
message = "My name is {name} and I am {age} years old.".format(**info)
print(message)

#Formatting Specifiers:
pi_value = 3.14159
formatted_pi = "The value of pi is {:.2f}".format(pi_value)
print(formatted_pi)

#Alignment and Width:
fruit_info = "{:<10} {:>5}".format("Apple", 3)
print(fruit_info)
# Apple        3

# Fill and Align Characters:
value = 42
padded_value = "Value: {:*^8}".format(value)
print(padded_value)
# Value: **42****

# Format String Literals (f-strings):更方便閱讀
name = "David"
age = 40
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
