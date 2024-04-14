# Your solution to Exercise 8
def even(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            continue
        if i < n-1:
            print(i, end=" ")
        elif i == n-1 or i == n:
            print(i)

n = int(input())
even(n)

# Same issue here:
# Function naming, parameter naming, and type hinting.

# The function name should be changed to `even_numbers` to make it more descriptive.
# Or ever better would be "print_even_numbers" to make it even more descriptive.

# The trick with the elif in `if i < n-1` is not needed. 
# The last `elif` statement can be changed to `else`.

# Approach is creative although.