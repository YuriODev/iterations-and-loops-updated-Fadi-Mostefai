# Your solution to Exercise 5

def intsum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = int(input())
print(intsum(n))

# Same issue here:
# Function naming, parameter naming, and type hinting.

# I would recommend to use naming such as "get_sum_of_integers" for the function
# or "get_sum". In this case such a short name is appropriate and quite 
# descriptive.

# Every time you use "return" in a function, you should annotate the function
# with the return type. In this case, the function is returning an integer, so
# you should annotate the function with "-> int" to indicate that the function
# is returning an integer.

# Also, I recommend to use "get_" prefix for functions that are returning some
# value, such as "get_sum_of_integers" or "get_sum". This is a common naming
# convention in Python and makes it clear that the function is returning a
# value.
