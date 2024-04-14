# Your solution to Exercise 37

def div(a, b):
    rem = 0
    count = 0
    while True:
        if a - b < 0:
            rem = a
            break
        a -= b
        count += 1
    return f"{count} {rem}"

a = int(input())
b = int(input())
print(div(a,b))

# Same Issue:
# Function naming, parameter naming, and type hinting

# Example how to improve:
# def division(dividend: int, divisor: int) -> str:
#     """Returns the quotient and remainder of the division of two numbers."""
#     remainder = 0
#     count = 0
#     while True:
#         if dividend - divisor < 0:
#             remainder = dividend
#             break
#         dividend -= divisor
#         count += 1
#     return f"{count} {remainder}"

# Even if you make a mistake, it will be always easier to read proper names
# rather than wasting your "mindfuel" what values are stored in a and b.
