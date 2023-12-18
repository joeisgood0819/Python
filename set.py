# Creating a set
my_set = {1, 2, 3, 4, 5}

# Duplicate values are automatically removed
my_set = {1, 2, 3, 2, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding an element to a set
my_set.add(6)

# Removing an element from a set
my_set.remove(3)

# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)

# Creating a frozen set
frozen_set = frozenset({1, 2, 3})

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(2 in my_set)  # Output: True
print(7 in my_set)  # Output: False

for element in my_set:
    print(element)

squares = {x**2 for x in range(5)}

#Operations
# Union
union_set = set1.union(set2)
# Intersection
intersection_set = set1.intersection(set2)
# Difference
difference_set = set1.difference(set2)

# Creating two sets
x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

# Union (x | y): Returns a new set containing all unique elements from both sets
union_set = x | y
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (x & y): Returns a new set containing common elements in both sets
intersection_set = x & y
print("Intersection:", intersection_set)  # Output: {4, 5}

# Symmetric Difference (x ^ y): Returns a new set containing elements that are unique to each set
symmetric_difference_set = x ^ y
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}
