#str.startswith(prefix), str.endswith(suffix)
sentence = "Python is powerful and versatile."
print(sentence.startswith("Python"))  # Output: True
print(sentence.endswith("versatile."))  # Output: True

#in
phrase = "Python is powerful."

print("Python" in phrase)    # Output: True
print("Java" in phrase)      # Output: False

#find
phrase = "Python is powerful and Python is easy."
print(phrase.find("Python"))  # Output: 0
print(phrase.find("is"))      # Output: 7
print(phrase.find("Java"))    # Output: -1 (not found)

#rfind
phrase = "Python is powerful and Python is easy."
print(phrase.rfind("Python"))  # Output: 20
print(phrase.rfind("is"))      # Output: 25
print(phrase.rfind("Java"))    # Output: -1 (not found)

#index
phrase = "Python is powerful and Python is easy."
print(phrase.index("Python"))  # Output: 0
print(phrase.index("is"))      # Output: 7
try:
    print(phrase.index("Java"))  # Raises ValueError
except ValueError as e:
    print(e)

#rindex
phrase = "Python is powerful and Python is easy."
print(phrase.rindex("Python"))  # Output: 20
print(phrase.rindex("is"))      # Output: 25
try:
    print(phrase.rindex("Java"))  # Raises ValueError
except ValueError as e:
    print(e)

#count
sentence = "Python is easy. Python is powerful."
print(sentence.count("Python"))  # Output: 2
print(sentence.count("Java"))    # Output: 0