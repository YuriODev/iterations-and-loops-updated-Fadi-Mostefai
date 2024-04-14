# Your solution to Exercise 41

def fib_digit(n):
    term1 = 0
    term2 = 1
    if n == 1:
        return term2
    else:
        term = 0
        for _ in range(n-1):
            term = term1 + term2
            term1 = term2
            term2 = term
        return term
    
n = int(input())
print(fib_digit(n))

# Same Issue:
# Function naming, parameter naming, and type hinting, return-else statement.

# Notes:
# 1. The function name and parameter name can be improved to:
#   - `get_fibonacci_number_at_position`
# 2. The return statement can be used to avoid else block, same as before
# 3. The code can be optimized to not use a loop to calculate the Fibonacci
#  number at a given position.
# 4. The function can be made more efficient by using a recursive approach.

# Example of refactored code:
# def get_fibonacci_number_at_position(position: int) -> int:
#     """Returns the Fibonacci number at the given position."""
#     if position == 0:
#         return 0
#     elif position == 1:
#         return 1
#     else:
#         return get_fibonacci_number_at_position(position - 1) + get_fibonacci_number_at_position(position - 2)
# You don't have to use recursion, but it's a good exercise to practice it.