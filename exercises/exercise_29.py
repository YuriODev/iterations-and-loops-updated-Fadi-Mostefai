# Your solution to Exercise 29
def series():
    num = int(input())
    sum1 = num
    sum2 = num ** 2
    while sum1 != 0:
        num = int(input())
        sum1 += num
        sum2 += num ** 2
    return sum2

print(series())

# Same Issue:
# Function naming, parameter naming, and type hinting.

# Note: really confusing to figure out what "sum1" and "sum2" are doing here.
# Which might cause confusion to the reader and yourself in the future, especially
# During stress or when you're in a hurry like exams.

# Also, "sum_1" and "sum_2" are better names than "sum1" and "sum2" because it's
# easier to read and understand + PEP8 compliant.

# Don't foget to add spaces between lines of code with different purposes.
# It makes the code more readable and easier to understand.

# Better name for the function: get_series_sum

# Final note: Good job with the logic and the while loop! Keep it up!