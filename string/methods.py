#split
sentence = "Python is fun and Python is versatile."
words = sentence.split(" ")
print(words)
x = "Mississippi"
print(x.split("ss",1)) #第一參數找字，第二切割次數

#join
words = ["Python", "is", "awesome"]
sentence = " ".join(words) #可用隨意字取代空白
print(sentence)

#int, float
numeric_str = "123"
float_str = "12.34"

integer_value = int(numeric_str) #int可放第二參數代表2/8/16進位
float_value = float(float_str)

print(integer_value)   # Output: 123
print(float_value)     # Output: 12.34

#str.strip(), str.lstrip(), str.rstrip()
padded_text = "   Hello, World!   "
print(padded_text.strip())   # Output: Hello, World! -左右空白
print(padded_text.lstrip())  # Output: Hello, World!   -左空白
print(padded_text.rstrip())  # Output:   Hello, World! -又空白
print(padded_text.strip("He"))   #移除所選

# isdigit(), isalpha() 
numeric_str = "12345"
alphabetic_str = "Python"
alphanumeric_str = "Python123"

print(numeric_str.isdigit())      # Output: True
print(alphabetic_str.isalpha())   # Output: True
print(alphanumeric_str.isdigit()) # Output: False
print(alphanumeric_str.isalpha()) # Output: False

#islower(), isupper()
lowercase_str = "python"
uppercase_str = "PYTHON"

print(lowercase_str.islower())  # Output: True
print(uppercase_str.isupper())  # Output: True

#str.replace(old, new)
message = "Hello, World! Hello, Python!"
updated_message = message.replace("Hello", "Hi")
print(updated_message)


