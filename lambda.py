### LAMBDA  ####
# a lambda is a small, anonymous function defined using the lambda keyword. It is often used for creating small, throwaway functions that are only needed for a short period of time and typically consist of a single line of code.

# def example_method(n):
#     return lambda a : a * n

# variable_example = example_method(100)
# print(variable_example(2))

### BASIC LAMBDA ####
# 1.) 

# Write a lambda function that takes a number x and returns x^2.

def power_two(x):
    return lambda a : a**x

result = power_two(2)
# print(result(10))

# 2.) 

# Write a lambda function that takes two numbers and returns their product.

def prod_two(x, y):
    return (lambda a, b : a*b)(x, y)
result_2 = prod_two(2,3)
# print(result_2)

### SORTING WITH LAMBDA

# 3.) 

# You have a list of dictionaries representing people with name and age keys. Sort this list by age using a lambda function.
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]

sorted_people = sorted(people, key=lambda person:person['age'])
# print(sorted_people)

### FILTERING WITH LAMBDA AND FILTER

# 4.)

# Use a lambda function with filter to get all even numbers from a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers = list(even_numbers) 
# print(even_numbers)

# 5.)

# Use a lambda function with filter to keep only words that have more than 4 letters in a list of strings.
words = ['apple', 'banana', 'kiwi', 'mango', 'grape']
four_letters = filter(lambda x : len(x) > 4, words)
# print(list(four_letters))

### MAPPING WITH LAMBDA AND MAP

# 6.) 

# Use a lambda function with map to add 5 to each number in a list.
numbers = [1, 2, 3, 4, 5]
updated_numbers = map(lambda x: x + 5, numbers)
updated_numbers = list(updated_numbers)  # Convert the map object to a list
# print(updated_numbers)

# 7.)

#Use a lambda function with map to get the length of each word in a list of strings.
words_2 = ['python', 'java', 'c++', 'javascript']
word_len = map(lambda x : len(x), words_2)
print(list(word_len))

