x = [1, 2 ,3]
x = [2 , "two", [1, 2, 3], 1, 3, 3]
print (len(x))

x[-1] #後面數來第一個 [1 ,2 ,3]

#slice功能
print(x[0:4])
print(x[-2:-1])
print(x[-1:2]) #空list
print(x[:4])
print(x[2:])

y = x[:] #copy x list into y
y [0] = 'one'
print(x)
y = x
y [0] = 'one' #同步修改
print(x)

x[1:3] = ["one", "two", "three"] #可以更多也可以更少=直接取代替換

# Creating an empty list
my_list = []

# Append method adds an element to the end of the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Display the list after appending elements
print("After append:", my_list)

# Extend method adds elements from another iterable (e.g., list) to the end of the list
additional_elements = [4, 5, 6]
my_list.extend(additional_elements)

# Display the list after extending with additional elements
print("After extend:", my_list)

# Insert method inserts an element(10) at a specific index(1)
my_list.insert(1, 10)

# Display the list after inserting an element at index 1
print("After insert:", my_list)

# Delete an element by its index using the del statement
del my_list[2]

# Display the list after deleting the element at index 2
print("After del:", my_list)

# Remove method removes the first occurrence of a value
my_list.remove(5)

# Display the list after removing the value 5
print("After remove:", my_list)

# Reverse method reverses the elements of the list in place
my_list.reverse()

# Display the list after reversing its elements
print("After reverse:", my_list)

# Sort method sorts the elements of the list in ascending order
my_list.sort()

# Display the list after sorting in ascending order
print("After sort:", my_list)

# Sorted function returns a new sorted list without modifying the original list
sorted_list = sorted(my_list)

# Display the sorted list without modifying the original list
print("Sorted list:", sorted_list)
print("Original list:", my_list)

#自定義排序 速度較慢能不用就不用

# Define a function named compare_num_of_chars
def compare_num_of_chars(string1):
    # The len() function returns the length (number of characters) of the input string
    return len(string1)

# Call the function with a string argument
result = compare_num_of_chars("Hello, World!")

# Print the result
print("Number of characters:", result)

#Number of characters: 13

# Creating a list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# The 'in' keyword checks if a value is present in the list
is_present = 5 in numbers
print("Is 5 present in the list?", is_present)

# The '+' operator concatenates two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# The '*' operator repeats a list a certain number of times
repeated_list = list1 * 3
print("Repeated list:", repeated_list)

# The 'None' keyword represents the absence of a value or a null value
empty_list = None
print("Empty list:", empty_list)

# The 'min' function returns the minimum value in a list
minimum_value = min(numbers)
print("Minimum value:", minimum_value)

# The 'max' function returns the maximum value in a list
maximum_value = max(numbers)
print("Maximum value:", maximum_value)

# The 'index' method returns the index of the first occurrence of a value
index_of_9 = numbers.index(9)
print("Index of 9:", index_of_9)

# The 'count' method returns the number of occurrences of a value in the list
count_of_5 = numbers.count(5)
print("Count of 5:", count_of_5)




