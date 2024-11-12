### REDUCING WITH LAMBDA AND REDUCE ###
# The reduce function from functools allows you to apply a function to a sequence cumulatively to reduce it to a single value.

# 8.)

# Use a lambda function with reduce to calculate the product of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
# print(product)

### HIGHER-ORDER LAMBDA FUNCTIONS ##

# 9.)

# Write a function make_multiplier(n) that returns a lambda function. This lambda should take a single argument x and return x * n.
# multiplier = make_multiplier(5)
# print(multiplier(10))  
# Should output 50
def make_multiplier(n):
    return lambda x: x * n

# Create a multiplier function that multiplies by 5
multiplier = make_multiplier(5)

# Test the function by multiplying 10 by 5
# print(multiplier(10))  
# Output: 50



### NESTED LAMBDA FUNCTIONS

# 10.)

#Create a lambda function that takes two numbers and returns a lambda function that adds the two numbers to any new number passed to it.
# Example usage:
adder = (lambda x, y: lambda z: x + y + z)(2, 3)
# print(adder(4))  
# Should output 9



### LAMBDA FUNCTIONS WITH CONDITIONALS

# 11.) 

# Write a lambda function that takes a number and returns “Even” if the number is even and “Odd” if the number is odd.

# num = input("enter an integer")
# if int(num) % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

## OR ##
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
    
# print(check_even_odd(4))

# 12.)

#Write a lambda function that takes a list of numbers and returns the maximum if the list has more than 3 elements; otherwise, it returns the minimum.

check_max_min = lambda lst: max(lst) if len(lst) > 3 else min(lst)

# Test the function
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [10, 20, 30]

print(check_max_min(numbers_1))  
print(check_max_min(numbers_2))