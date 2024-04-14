# Your solution to Exercise 21
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_factorial(n):
    sum = 0
    for i in range(1, n+1):
        sum += factorial(i)
    return sum

n = int(input())
print(sum_factorial(n))

# Same issue here:
# Function naming, parameter naming, and type hinting.

# Example how it could be improved:

# def get_factorial(num: int) -> int:
#     """Return the factorial of a number."""
#     if num == 1:
#         return 1
#     else:
#         return num * get_factorial(num-1)

# def get_sum_factorial(num: int) -> int:
#     """Return the sum of factorials from 1 to num."""
#     total_sum = 0
#     for i in range(1, num+1):
#         total_sum += get_factorial(i)
#     return total_sum


# n = int(input())
# print(get_sum_factorial(n))

# Note:
# For big numbers, the recursive function will not work because of the
# recursion limit. You can write decorator to track time and memory usage
# of the function for iterative and recursive functions.
