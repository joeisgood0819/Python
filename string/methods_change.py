#maketrans, translate 將不同語言翻譯
before = "~^()"
after = "!&{}"
translation_table = str.maketrans(before, after)

text = "~^()yz"
translated_text = text.translate(translation_table)
print(translated_text)  # Output: !&{}yz

#to lower and upper
text = "Hello, World!"
lower_text = text.lower()
print(lower_text)  # Output: hello, world!
text = "Hello, World!"
upper_text = text.upper()
print(upper_text)  # Output: HELLO, WORLD!

#to Capitalize
text = "python programming"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Python programming

#Title
text = "python programming is fun"
title_text = text.title()
print(title_text)  # Output: Python Programming Is Fun

#swapcase
mixed_case_text = "PyThOn Is FuN"
swapped_case = mixed_case_text.swapcase()
print(swapped_case)  # Output: pYtHoN iS fUn

#expandtabs(tabsize=8)
indented_text = "Hello\tWorld!"
expanded_text = indented_text.expandtabs(4)
print(expanded_text)

#str.ljust(width[10, fillchar])
text = "Hello"
left_justified = text.ljust(10, '-')
print(left_justified)  # Output: Hello-----

#str.rjust(width[10, fillchar])
text = "Hello"
left_justified = text.ljust(10, '-')
print(left_justified)  # Output: -----Hello

#str.center(width[10, fillchar])
text = "Hello"
centered = text.center(10, '-')
print(centered)  # Output: --Hello---

#str.zfill(width)
number = "42"
zero_padded = number.zfill(5)
print(zero_padded)  # Output: 00042

#str.reverse()
text = "Hello, World!"
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: !dlroW ,olleH
