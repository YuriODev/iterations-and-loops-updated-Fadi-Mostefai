# Your solution to Exercise 27

def picalc(n):
    Pi = 0
    count = 1
    for _ in range(n):
        if count % 4 == 1:
            Pi += 4/count
        elif count % 4 == 3:
            Pi -= 4/count
        count += 2
    return Pi

n = int(input())
print(picalc(n))

# Same Issue:
# Function naming, parameter naming, and type hinting.

# Note:
# be careful with using "Pi" or "pi", it can trigger a false positive in some linters.
# Approach with the modulo was a bit complicated, but well handled. 
# Have a look at the solution for a more straightforward approach.

# About naming, you could use "pi_calc" instead of "picalc" for better readability.
# Better to name it as "get_pi_value" or "calculate_pi" to make it more descriptive.

# In Python starting a variable name with a capital letter is not recommended,
# as it is reserved for class names.