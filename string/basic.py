# 1. String Creation:
# Strings can be created using single quotes ('), double quotes ("), or triple quotes (''' or """) for multiline strings.
single_quoted = 'Hello, World!'
double_quoted = "Python is fun!"
multiline = '''This is a
multiline string.'''

# 2. String Concatenation:
# Strings can be concatenated using the + operator.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# 3. String Indexing and Slicing:
# Access individual characters using indexing and extract substrings using slicing.
message = "Hello, Python!"
first_char = message[0]  # 'H'
substring = message[7:13]  # 'Python'

#4. String Methods:
# Strings have various built-in methods for manipulation and formatting.
greeting = "   Hello, World!   "
lowercase = greeting.lower()
uppercase = greeting.upper()
stripped = greeting.strip()

# 5. String Formatting:
# Use formatting to create formatted strings with placeholders.
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)

# 6. String Escape Characters:
# Escape characters are used to represent special characters.
escaped_string = "This is a line with a newline character.\nAnd this is the next line."

# 7. String Methods for Searching and Counting:
# Methods like find, count, and replace can be used for searching and replacing.
sentence = "Python is easy to learn. Python is powerful."
position = sentence.find("Python")
occurrences = sentence.count("Python")
replaced = sentence.replace("Python", "Java")

# 8. String Formatting (f-strings):
# Introduced in Python 3.6, f-strings provide a concise way to format strings.
name = "Bob"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."



