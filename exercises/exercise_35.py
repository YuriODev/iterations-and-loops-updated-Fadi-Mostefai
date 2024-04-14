# Your solution to Exercise 35
def odd(n):
    upper_bound = (10 ** n) - 1
    lower_bound = (10 ** (n-1)) - 1
    for i in range(upper_bound, lower_bound, -2):
        print(i, end=" ")
    print()

n = int(input())
odd(n)

# Same Issue:
# Function naming, parameter naming, and type hinting

# Note:
# Variable naming is way better now, but the function name and parameter name can be improved.