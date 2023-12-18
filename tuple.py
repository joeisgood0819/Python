# Creating a tuple
my_tuple = (1, 'two', 3.0)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1

# Attempting to modify a tuple will raise an error
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Tuple packing
packed_tuple = 1, 'two', 3.0

# Tuple unpacking
a, b, c = packed_tuple

# Tuple packing Cases
# Packing
student_info = ('John Doe', 25, 'Computer Science')

# Unpacking
name, age, major = student_info

# Displaying the unpacked values
print("Name:", name)
print("Age:", age)
print("Major:", major)

#自動解包功能
x = (1, 2, 3, 4)
a, b, *c = x
print("a:", a)
print("b:", b)
print("c:", c)
a: 1
b: 2
c: [3, 4]

single_element_tuple = (42,)

# Using count to count occurrences of a value
count_of_two = my_tuple.count('two')  # Output: 1

# Using index to find the index of a value
index_of_three = my_tuple.index(3.0)  # Output: 2

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

# Comparing tuples
print(tuple1 == tuple2)  # Output: False


