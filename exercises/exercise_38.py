# Your solution to Exercise 38

def even_diff(n):
    large = 0
    small = 0
    if n == 0:
        return False
    else:
        while n != 0:
            last_digit = n % 10
            n = n // 10
            if last_digit > large:
                if small == 0:
                    small = large
                large = last_digit
            elif small == 0:
                small = last_digit
            elif last_digit < small:
                small = last_digit
        return True if (large - small) % 2 == 0 else False

n = int(input())
print(even_diff(n))

# Same Issue:
# Function naming, parameter naming, and type hinting.

# Notes:
# 1. The function name and parameter name can be improved to:
#   - `is_even_difference`
# prefix "is" is used to indicate that the function returns a boolean value.
# 2. Return statement can be used to avoid else block, same as before
# 3. The final return statement can be simplified to:
# return (large - small) % 2 == 0 
# since the condition is already a boolean expression.

# Example of refactored code:
# def is_even_difference(number: int) -> bool:
#     """Returns True if the difference between the largest and smallest digit of a number is even, otherwise False."""
#     largest_digit = 0
#     smallest_digit = 0
#     if number == 0:
#         return False
#     while number != 0:
#         last_digit = number % 10
#         number //= 10
#         if last_digit > largest_digit:
#             if smallest_digit == 0:
#                 smallest_digit = largest_digit
#             largest_digit = last_digit
#         elif smallest_digit == 0:
#             smallest_digit = last_digit
#         elif last_digit < smallest_digit:
#             smallest_digit = last_digit
#     return (largest_digit - smallest_digit) % 2 == 0

# Also, you can see the use of "//=" operator to perform floor division in the code.
