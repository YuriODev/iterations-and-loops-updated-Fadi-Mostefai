# Your solution to Exercise 31

def temp_checker(d):
    temp = 0
    for _ in range(d):
        num = int(input())
        if num < temp:
            temp = num
    return f"{temp}\nYes" if temp < -18 else f"{temp}\nNo"

d = int(input())
print(temp_checker(d))

# Same Issue:
# Function naming, parameter naming, and type hinting, temp variable

# Note:
# Brilliant approach for using ternary operator for the return statement!