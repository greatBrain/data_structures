# There are two ways of copying objects: Shallow and deeep. 

# Shallow copy example:
from copy import copy

# Original object
numbers = [num for num in range(1,10)]

# Copied object
numbers_copy = copy(numbers)

