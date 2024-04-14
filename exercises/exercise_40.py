# Your solution to Exercise 40

def fibonacci(n):
    fibonacci_seq = "1"
    term1 = 0
    term2 = 1
    while True:
        term = term1 + term2
        if term >= n:
            break
        fibonacci_seq += " " + str(term)
        term1 = term2
        term2 = term
    return fibonacci_seq

n = int(input())
print(fibonacci(n))

# Same Issue:
# Function naming, parameter naming, and type hinting

# Notes:
# The code could be optimized to not use string for storing the
# Fibonacci sequence, which would make it easier to manipulate and work with
# the individual terms.

# Naming is a bit inconsistent and confusing, as you use `term` for the current term,
# but `term1` and `term2` for the previous terms. It would be clearer to name them
# `current_term`, `previous_term1`, and `previous_term2`.

# Example of refactored code:
# def print_fibonacci_sequence(n: int) -> None:
#    """Prints the Fibonacci sequence up to the given number n."""
#    previous_term1 = 0
#    previous_term2 = 1
#    while True:
#        current_term = previous_term1 + previous_term2
#        if current_term >= n:
#            break
#        print(current_term, end=" ")
#        previous_term1, previous_term2 = previous_term2, current_term

# n = int(input())
# print_fibonacci_sequence(n)

# It'd be better to print the Fibonacci sequence directly, rather than
# returning it as a string.