# Your solution to Exercise 12
def sum(n):
    sum = 0
    for i in range(100, 1000):
        if i % n != 0:
            continue
        sum += i
    return sum

n = int(input())
print(sum(n))

# Same issue here:
# Function naming, parameter naming, and type hinting.

# A few important things to note here:
# 1) You must be very careful with the naming of your functions and parameters.
# Since you are using "sum" as a variable name, you should not use it as a
# function or variable name, as it will overwrite the built-in sum function.

# It worked out fine in this case, but it's a good practice to avoid using
# built-in function names as variable names.

# For example (error):
# list = [1, 2, 3, 4, 5]
# sum = 0
# a = int(input())
# list += a
# sum += sum(list)
# How many errors can you find in the above code? :D 