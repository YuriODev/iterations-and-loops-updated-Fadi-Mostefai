# Your solution to Exercise 39

def digit(n):
    sum = 0
    if n < 0:
        n = n * -1
    while n != 0:
        last_digit = n % 10
        n = n // 10
        sum += last_digit
    return sum

n = int(input())
print(digit(n))

# Same Issue:
# Function naming, parameter naming, and type hinting.

# Well done with handling negative numbers!
# Don't hesitate to use operators like `*=` to simplify the code.
# If you notice, you are using "+=" operator to add the last digit to the sum.
# But you don't use the `*=` operator to multiply the number by -1 and "//=" operator to perform floor division.
# Which makes your code less consistent.