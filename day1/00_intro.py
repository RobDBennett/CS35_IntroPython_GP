
# This is a comment

# lets print a string
print("Hello, CS35!", "Some other text", "and theres more...", end="\t")
# variables
# label = value
# let const var (js)
# int bool short (c)
first_name = "Rob"
print("Hello CS35 and" , first_name)
num = 23.87

# # f strings
my_string = "    this is a string tom            "
print(my_string)

print(my_string.strip())
print(len(my_string))
print(len(my_string.strip()))

print(f"Hello CS35 and                {first_name}.......")
print("something on a new line")




# collections

# create an empty list? Array

my_list = []

print(my_list)

# create a list with numbers 1, 2, 3, 4, 5
lst1 = [1, 2, 3, 4, 5]
# add an element 24 to lst1

lst1.append(24)

lst1.append(0, 12)

print(lst1)

# # print all values in lst2
# print(lst2)


# loop over the list using a for loop


# while loop
for i in range(len(lst1)):
    print(lst1[i])

# List Comprehensions

# Create a new list containing the squares of all values in 'numbers'
numbers = [1, 2, 3, 4]

# List comprehension
squares = [num * num for num in numbers]

# For loop.
for num in numbers:
    squares.append(num * num)

print(numbers)
print(squares)

# Filtering with a list comprehension
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        pass

evens = [num for num in numbers if num % 2 == 0]

# create a new list of even numbers using the values of the numbers list as inputs

print(evens)

# create a new list containing only the names that start with 's' make sure they are capitalized (regardless of their original case)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy"]
s_names = [name.capitalize() for name in name if name[0].lower() == 's']
print(s_names)


# Dictionaries

# Create a new dictionary

dictionary = {'One': 1, 'Two':2, 'Three':3}
# empty

# key value pairs

# access an element via its key
print(dictionary['One'])